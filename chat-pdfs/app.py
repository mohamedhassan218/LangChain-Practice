import os
import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceHubEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain_community.llms import HuggingFaceEndpoint
from custom_templates import css, bot_template, user_template


load_dotenv()
repo_id = os.environ["REPO_ID"]
huggingface_token = os.environ["HUGGINGFACEHUB_API_TOKEN"]
# repo_id = "mistralai/Mistral-7B-Instruct-v0.2"


def get_pdf_text(pdf_docs):
    """
    @code:
        row_text = get_pdf_text(pdf_documents)

    @param:
        pdf_docs: represents the doc or docs taken from the user.

    @return:
        text: which is a string represents the whole content of the all PDFs.
    """
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text


def get_text_chunks(row_text):
    """
    @code:
        chunks = get_text_chunks(row_text)

    @param:
        row_text: a string that represents the content that we wanna to split into chunks.

    @return:
        chunks: list of splited chunks from the original row_text.
    """
    text_splitter = CharacterTextSplitter(
        separator="\n", chunk_size=1000, chunk_overlap=200, length_function=len
    )
    chunks = text_splitter.split_text(row_text)
    return chunks


def get_vectorstore(text_chunks):
    """
    @code:
        vectorstore = get_vectorstore(text_chunks)

    @param:
        text_chunks: a list of strings each of them represents a chunk of the original text.

    @return:
        vectorstore: a vector database contain the embedding of our chunks.
    """
    embeddings = HuggingFaceHubEmbeddings()
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore


def get_conversation(vectorstore, repo_id, huggingface_token):
    llm = HuggingFaceEndpoint(
        repo_id=repo_id, max_length=128, temperature=0.5, token=huggingface_token
    )
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    conversation_chain = ConversationalRetrievalChain(
        llm=llm, retriever=vectorstore.as_retriever(), memory=memory
    )
    return conversation_chain


def handle_user_prompt(user_question):
    response = st.session_state.conversation({"question": user_question})
    st.session_state.chat_history = response["chat_history"]

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(
                user_template.replace("{{MSG}}", message.content),
                unsafe_allow_html=True,
            )
        else:
            st.write(
                bot_template.replace("{{MSG}}", message.content),
                unsafe_allow_html=True,
            )


def main():
    # load_dotenv()
    st.set_page_config(page_title="Chat with PDFs", page_icon="robot.png")
    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    st.header("Chat with your PDFs :books:")
    user_question = st.text_input("Enter a prompt . . . ")

    if user_question:
        handle_user_prompt(user_question)

    with st.sidebar:
        st.subheader("Your documents")
        pdf_docs = st.file_uploader("Upload your docs here", accept_multiple_files=True)

        if st.button("Process"):
            with st.spinner("Processing . . ."):
                # Get pdf row text.
                row_text = get_pdf_text(pdf_docs)

                # Get the chunks of our text.
                text_chunks = get_text_chunks(row_text)

                # Create vector store.
                vectorstore = get_vectorstore(text_chunks)

                # Create conversation chain.
                conversation = get_conversation(vectorstore, repo_id, huggingface_token)


if __name__ == "__main__":
    main()