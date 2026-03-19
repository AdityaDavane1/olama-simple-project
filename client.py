import requests
import streamlit as st


def get_groq_response(input_text, language):
    json_body = {
        "input": {
            "language": language,
            "text": input_text
        },
        "config": {},
        "kwargs": {}
    }

    response = requests.post(
        "http://127.0.0.1:8000/chain/invoke",
        json=json_body
    )

    return response.json()['output']


st.title("LLM Application Using LCEL")

language = st.selectbox(
    "Select Language",
    ["French", "Hindi", "Spanish", "German", "Japanese", "Marathi"]
)

input_text = st.text_input("Enter text to translate")

if input_text:
    result = get_groq_response(input_text, language)
    st.write(result)