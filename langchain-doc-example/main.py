# Import our libraries that we wanna use it.
import os
from getpass import getpass
from langchain_community.llms import HuggingFaceEndpoint
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

# Define the repository ID for the Hugging Face model.
repo_id = os.environ["REPO_ID"]

# Get our Hugging Face token from the .env file.
HUGGINGFACEHUB_API_TOKEN = os.environ["HUGGINGFACEHUB_API_TOKEN"]

# Ask simple question.
question = "Give me five main subjects must the computer science student learn to be a professional software engineer"

# Build a template to our prompt manually.
template = """Question: {question}\n
                Answer: Let's think step by step."""

# Create a prompt template using the defined template.
prompt = PromptTemplate.from_template(template)

# Initialize the HuggingFaceEndpoint with necessary parameters.
llm = HuggingFaceEndpoint(
    repo_id=repo_id, max_length=128, temperature=0.5, token=HUGGINGFACEHUB_API_TOKEN
)

# Create an LLMChain instance with the defined prompt and HuggingFaceEndpoint.
llm_chain = LLMChain(prompt=prompt, llm=llm)

# Run the LLMChain with the provided question and print the result.
response = llm_chain.invoke(question)
print(response['text'])

"""
THE OUTPUT:
    A professional software engineer should have a solid foundation in computer science concepts and practical skills in programming, data structures and algorithms, software design, and software development methodologies.
    Here are the five main subjects a computer science student should learn to be a professional software engineer:
        1. Programming Fundamentals:
           - Mastering at least one programming language and its syntax, semantics, and standard libraries.
           - Understanding data types, control structures, functions, and classes.
           - Learning to write clean, efficient, and maintainable code.
        2. Data Structures and Algorithms:
           - Understanding common data structures like arrays, linked lists, trees, hash tables, and graphs.
           - Learning algorithms for sorting, searching, graph traversal, and dynamic programming.
           - Understanding time and space complexity analysis.
        3. Software Design:
           - Learning software design principles like separation of concerns, encapsulation, inheritance, and polymorphism.
           - Understanding design patterns and their use cases.
           - Learning to create well-designed software components and systems.
        4. Software Development Methodologies:
           - Understanding Agile methodologies like Scrum and Kanban.
           - Learning to work in a team, communicate effectively, and manage project scope, time, and resources.
           - Understanding the importance of testing, debugging, and continuous integration.
        5. Operating Systems and System Programming:
           - Understanding the basics of operating systems, file systems, and process management.
           - Learning low-level programming concepts like memory management, input/output, and system calls.
           - Understanding the role of the operating system in software development and deployment.
"""