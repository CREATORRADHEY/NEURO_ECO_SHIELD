import streamlit as st
import google.generativeai as genai


st.set_page_config(page_title="NOVA CHAT", page_icon="🤖", layout="wide")

st.title("🤖 NOVA CHAT")
st.markdown("### Powered by Google Gemini AI")
st.divider()


key = "AIzaSyCE3kNpK_VQ-h6H57NkO4SzMfC7o6-rAd8"
genai.configure(api_key=key)
model = genai.GenerativeModel("gemini-2.0-flash")


with st.sidebar:
    st.header("⚙️ Settings")
    st.write("**Model:** Gemini 2.0 Flash")
    
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.chat_history = []
        st.rerun()
    
    st.divider()
    st.markdown("### 📊 Stats")
    if "chat_history" in st.session_state:
        total = len(st.session_state.chat_history)
        st.metric("Total Messages", total)


if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_input = st.chat_input("💬 Type your message here...")

if user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    
    with st.chat_message("user"):
        st.write(user_input)
    
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = model.generate_content(user_input)
                ai_response = response.text
                st.session_state.chat_history.append({"role": "assistant", "content": ai_response})
                st.write(ai_response)
            except Exception as e:
                st.error(f"Error: {str(e)}")
