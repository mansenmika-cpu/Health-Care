import streamlit as st
import google.generativeai as genai

st.markdown("""
    <style>
    .stApp {
        background-color: #f0f8ff;
    }
    .stChatMessage {
        border-radius: 15px;
        padding: 10px;
        margin-bottom: 10px;
    }
    /* Simple footer disclaimer */
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: white;
        color: gray;
        text-align: center;
        padding: 10px;
        font-size: 12px;
        border-top: 1px solid #e6e6e6;
    }
    </style>
    <div class="footer">
        ⚠️ <b>Disclaimer:</b> This AI is for informational purposes only and is not a substitute for professional medical advice.
    </div>
    """, unsafe_allow_html=True)

system_instruction = """
You are a specialized Health Care Assistant. 
1. ONLY answer questions related to health, medicine, wellness, and biology.
2. If a user asks about anything else (politics, coding, sports, etc.), politely 
   refuse and state that you are only programmed for healthcare assistance.
3. Always include a disclaimer that you are an AI, not a doctor.
"""

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel(
    model_name='gemini-2.5-flash',
    system_instruction=system_instruction
)


col1, col2 = st.columns([0.1, 0.9])
with col1:
    st.markdown("## 🩺")
with col2:
    st.title("Health Care Assistant")

st.info("Ask me about symptoms, medications, or wellness tips. I am strictly programmed for healthcare assistance.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("How can I help you today?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            chat = model.start_chat(history=[])
            response = chat.send_message(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:

            st.error(f"Error: {e}")

