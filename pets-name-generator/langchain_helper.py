import os
import streamlit as st
from langchain_community.llms import HuggingFaceHub
from langchain_community.llms import HuggingFaceEndpoint
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from dotenv import load_dotenv

# Load environment variables.
load_dotenv()

# Get the token and repo id.
repo_id = os.environ["REPO_ID"]
hugging_face_token = os.environ["HUGGINGFACEHUB_API_TOKEN"]

"""
    Function that takes in the animal type and it's color and 
    speak to our llm and return the response.
"""
def generate_pet_name(animal_type, pet_color):
    llm = HuggingFaceEndpoint(
        repo_id=repo_id, temperature=0.7, token=hugging_face_token
    )
    prompt_template_name = PromptTemplate(
        input_variables=["animal_type", "pet_color"],
        template="I have a {animal_type} pet and I want a cool name for it, it is {pet_color} in color. Suggest me five cool names for my pet.",
    )
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="pet_name")

    response = name_chain({"animal_type": animal_type, "pet_color": pet_color})
    return response


# Just for debuging.
if __name__ == "__main__":
    response = generate_pet_name("Dog", "Black")
    print(response['pet_name'])