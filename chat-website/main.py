import os
import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceHubEmbeddings
from langchain_community.llms import HuggingFaceEndpoint
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains.combine_documents import create_stuff_documents_chain


# Grap our environment variables.
load_dotenv()
repo_id = os.environ["REPO_ID"]
HUGGINGFACEHUB_API_TOKEN = os.environ["HUGGINGFACEHUB_API_TOKEN"]


def get_response(user_prompt):
    return "I do not know"


def get_vectorstore_from_url(url):
    # Get the whole text from the website.
    loader = WebBaseLoader(url)
    doc = loader.load()

    # Split our text into chunks.
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
        length_function=len,
        is_separator_regex=False,
    )
    chunks = text_splitter.split_documents(doc)

    # Create vectorstore from the chunks.
    embeddings = HuggingFaceHubEmbeddings()
    vector_store = Chroma.from_documents(chunks, embeddings)
    return vector_store


def get_context_retriever_chain(vectorstore):

    llm = HuggingFaceEndpoint(
        repo_id=repo_id, max_length=128, temperature=0.7, token=HUGGINGFACEHUB_API_TOKEN
    )

    retriever = vectorstore.as_retriever()

    prompt = ChatPromptTemplate.from_messages(
        [
            MessagesPlaceholder(variable_name="chat_history"),
            ("user", "{input}"),
            (
                "user",
                "Given the above conversation, generate a search query to look up in order to get information relevant to the conversation",
            ),
        ]
    )

    retriever_chain = create_history_aware_retriever(llm, retriever, prompt)
    return retriever_chain


def get_conversational_rag_chain(retriever_chain):
    llm = HuggingFaceEndpoint(
        repo_id=repo_id, max_length=128, temperature=0.7, token=HUGGINGFACEHUB_API_TOKEN
    )

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "Answer the user's questions based on the below context: \n\n{context}",
            ),
            MessagesPlaceholder(variable_name="chat_history"),
            ("user", "{input}"),
        ]
    )

    stuff_document_chain = create_stuff_documents_chain(llm, prompt)
    return create_retrieval_chain(retriever_chain, stuff_document_chain)


# App configuration.
st.set_page_config(page_title="Chat with website", page_icon="🔗")
st.title("Chat with website")

# Our sidebar.
with st.sidebar:
    st.header("Settings")
    url = st.text_input("Website URL")

# Activate the chat only if the user entered an URL.
if url is None or url == "":
    st.info(body="You must enter URL", icon="🚨")
else:
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [AIMessage(content="Hello, How can I help U?")]
    if "vectorstore" not in st.session_state:
        st.session_state.vectorstore = get_vectorstore_from_url(url)

    retriever_chain = get_context_retriever_chain(st.session_state.vectorstore)

    conversation_rag_chain = get_conversational_rag_chain(retriever_chain)

    # Take user prompt.
    user_prompt = st.chat_input("Enter your prompt . . .")
    if user_prompt is not None and user_prompt != "":
        # response = get_response(user_prompt)
        response = conversation_rag_chain.invoke(
            {"chat_history": st.session_state.chat_history, "input": user_prompt}
        )

        # st.write(response)

        st.session_state.chat_history.append(HumanMessage(content=user_prompt))
        st.session_state.chat_history.append(AIMessage(content=response["answer"]))

    # Grap whole messages.
    for message in st.session_state.chat_history:
        if isinstance(message, AIMessage):
            with st.chat_message("AI"):
                st.write(message.content)
        elif isinstance(message, HumanMessage):
            with st.chat_message("Human"):
                st.write(message.content)