# Overview
This is the second project done in this [tutorial](https://youtu.be/lG7Uxts9SXs?si=fa3o3XKhu21Y4VmG) from freeCodeCamp. In the video, he used OpenAI but here we're using a Hugging Face open-source model.

It simply takes the URL of a youtube video, extract the transcript of the video, embedd it and takes user's prompt and use the vector store to answer this prompt.

> Note: the quality of your response depends on the quality of the model you'll use. So make sure to choose it carefully!


# Getting Started
1. Clone the Repository:
    ``` bash
    git clone https://github.com/mohamedhassan218/LangChain-Practice
    cd LangChain-Practice/youtube-assistant
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
    REPO_ID=repo_id
    HUGGINGFACEHUB_API_TOKEN=your_huggingface_api_token
    ```


6. Run the Project:
    ``` bash
    streamlit run main.py
    ```


# Demo

![Demo](Demo.gif)

> Note: Make sure to keep your `.env` file and any sensitive information, such as API tokens, private. Do not push them to your GitHub repository for security reasons.


Feel free to take the code, customize it and try different ideas.