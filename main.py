import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyA83yuYtrFGGjdRTPfuNiZwtog-fTLEkkM")
def ai(txt):

    for m in genai.list_model():
        if'generateContent' in m.support_generation_methods:
            print(m.name)
    model = genai.GenerativeModel('gemini-pro')
    return response.text



st.title(" Mohanraj AI Assistant")

command =st.chat_input("how can i help ?")

if "message" not in st.session_state:
    st.session_state.message = []

for chat in st.session_state.message:
    with st.chat_message(chat["role"]):
        st.write(chat["message"])

if command:
    with st.chat_message("USER"):
        st.write(command)
        st.session_state.message.append({"role":"USER","message":"command"})
    if "hello" in command:
        with st.chat_message("Bot"):
            st.write("hi how are you ?")
            st.session_state.message.append({"role":"Bot","message":"hi how are you ?"})
    elif "who" in command:
        with st.chat_message("Bot"):
            st.write("Im mohanraj AI assistant")
            st.session_state.message.append({"role":"Bot","message":"Im mohanraj AI assistant"})

    else:
        with st.chat_message("Bot"):
            data = ai(command)
            st.write(data)
            st.session_state.message.append({"role":"Bot","messgae":"data"})
print(st.session_state.message)





