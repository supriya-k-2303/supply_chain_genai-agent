import streamlit as st
import requests



API_URL = "http://127.0.0.1:8000/chat"



st.set_page_config(
    page_title="Supply Chain AI Agent",
    page_icon="🚚",
    layout="centered"
)



st.title("🚚 Supply Chain GenAI Agent")

st.write(
    "Ask questions about supply chain, inventory, suppliers, sales and deliveries."
)



if "messages" not in st.session_state:

    st.session_state.messages = []



# Display previous chat

for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):

        st.markdown(
            message["content"]
        )



# User input

question = st.chat_input(
    "Ask your question..."
)



if question:


    # user message

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )


    with st.chat_message("user"):

        st.markdown(question)



    # API call

    try:

        response = requests.post(
            API_URL,
            json={
                "question": question
            },
            timeout=120
        )


        if response.status_code == 200:

            answer = response.json()["answer"]

        else:

            answer = (
                f"API Error: {response.status_code}"
            )


    except Exception as e:

        answer = (
            f"Connection error: {str(e)}"
        )



    # assistant response

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )


    with st.chat_message("assistant"):

        st.markdown(answer)