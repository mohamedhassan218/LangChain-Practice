# Overview
This project is done in this [tutorial](https://youtu.be/bupx08ZgSFg?si=x98-LQ9SMsl4hMUZ). I strongly recommend it for anyone, it helped me to grap many things and I've added somethings in addition to all code from this video.

It simply takes your URL, scrapping it, and embeddings the data in your website and use them as a context to be able to response to your prompt.

> Note: the quality of your response depends on the quality of the model you'll use. So make sure to choose it carefully!


# Getting Started
1. Clone the Repository:
    ``` bash
    git clone https://github.com/mohamedhassan218/LangChain-Practice
    cd LangChain-Practice/chat-website
    ```


2. Create a Virtual Environment:
    ```bash
    python -m venv .venv
    ```

3. Activate the Virtual Environment:
    - On Windows:
        ```bash
        .venv\Scripts\activate
        ```

    - On Unix or MacOS:
        ```bash
        source .venv/bin/activate
        ```


4. Install Dependencies:
    ``` bash
    pip install -r requirements.txt
    ```


5. Set up Environment Variables:
    Create a `.env` file in the project root and add the following variables:
    ```
    HUGGINGFACEHUB_API_TOKEN=""
    REPO_ID=""
    ```


6. Run the Project:
    ``` bash
    streamlit run main.py
    ```


# Demo

The url on this demo is a definition about the LangChain framework, you can find it [here](https://www.techtarget.com/searchenterpriseai/definition/LangChain).

![Demo](Demo.png)



Feel free to take the code, customize it and try different ideas.