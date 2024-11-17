from dotenv import load_dotenv
from langchain_ollama import OllamaLLM
import streamlit as st

try:
    #LOAD API KEYS
    load_dotenv()

    #INITIALIZE LLM
    ollama_llm = OllamaLLM(model='llama3.2:1b')

    if "conversation_history" not in st.session_state:
        st.session_state.conversation_history = []

    conversation_context = [("system", 
                             "You are an expert assistant, \
                              providing clear, detailed, and \
                              accurate answers. "
                             "Keep responses relevant and focused, \
                              avoiding unnecessary information.\
                              Always aim to be helpful and engaging.")]

    st.title("Q&A WITH LLAMA3")
    prompt = st.chat_input(placeholder='Message Llama')

    if prompt:
        st.write('You:', prompt)
        st.session_state.conversation_history.append(("user", prompt))

        for role, message in st.session_state.conversation_history:
            conversation_context.append((role, message))

        formatted_prompt = "\n".join([f"{role}: {message}" \
            for role, message in conversation_context])

        response = ollama_llm.invoke(formatted_prompt)
        st.write("LLama:", response)
        st.session_state.conversation_history.append(("llama", response))

except Exception as e:
    st.error(f"Error: {e}")
