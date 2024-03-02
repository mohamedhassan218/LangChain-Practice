# Overview
This is a simple project that demonstrates the use of the LangChain library to build a Language Model (LLM) chain using Hugging Face models. The project focuses on asking a question and obtaining a detailed answer in multiple steps.

# Getting Started

1. Clone the Repository:
    ``` bash
    git clone https://github.com/mohamedhassan218/LangChain-Practice
    cd LangChain-Practice/langchain-doc-example
    ```


2. Create a Virtual Environment:
    ```bash
    python -m venv .venv
    Activate the Virtual Environment:
    ```

    - On Windows:
        ```bash
        .venv\Scripts\activate
        ```

    - On Unix or MacOS:
        ```bash
        source .venv/bin/activate
        ```


3. Install Dependencies:
    ``` bash
    pip install langchain python-dotenv huggingface_hub
    ```


4. Set up Environment Variables:
Create a `.env` file in the project root and add the following variables:

    ```
    REPO_ID=repo_id
    HUGGINGFACEHUB_API_TOKEN=your_huggingface_api_token
    ```


5. Run the Project:
    ``` bash
    python main.py
    ```


Feel free to customize the code and explore different questions and prompts by changing the value of the `question` variable.

> Note: Make sure to keep your `.env` file and any sensitive information, such as API tokens, private. Do not push them to your GitHub repository for security reasons.