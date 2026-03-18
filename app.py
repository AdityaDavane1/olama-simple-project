import streamlit as st
from model import get_response

st.set_page_config(
    page_title="AI Assistant",
    page_icon="✦",
    layout="centered"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap');

* { font-family: 'Inter', sans-serif; }

.stApp { background: #fafafa; }

#MainMenu, footer, header { visibility: hidden; }

.stTextInput label {
    font-size: 13px !important;
    font-weight: 500 !important;
    color: #444 !important;
}
.stTextInput input {
    background: #fff !important;
    border: 1.5px solid #e5e7eb !important;
    border-radius: 10px !important;
    padding: 14px 16px !important;
    font-size: 14px !important;
    color: #111 !important;
    box-shadow: 0 1px 3px rgba(0,0,0,0.04) !important;
}
.stTextInput input:focus {
    border-color: #2563eb !important;
    box-shadow: 0 0 0 3px rgba(37,99,235,0.08) !important;
}
.stButton button {
    background: #111 !important;
    color: #fff !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 12px 28px !important;
    font-size: 13px !important;
    font-weight: 500 !important;
    width: 100% !important;
    margin-top: 4px !important;
}
.stButton button:hover { background: #2563eb !important; }
.answer-card {
    background: #fff;
    border: 1.5px solid #e5e7eb;
    border-radius: 14px;
    padding: 24px 28px;
    margin-top: 24px;
    box-shadow: 0 2px 12px rgba(0,0,0,0.04);
}
.answer-dot {
    width: 8px; height: 8px;
    background: #22c55e;
    border-radius: 50%;
    display: inline-block;
    margin-right: 8px;
}
.answer-label {
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: #999;
}
.answer-text {
    font-size: 14px;
    color: #333;
    line-height: 1.8;
    margin-top: 12px;
}
.footer {
    text-align: center;
    font-size: 11px;
    color: #ccc;
    margin-top: 60px;
}
</style>
""", unsafe_allow_html=True)

# ── Header ────────────────────────────────────────────────
st.markdown("""
<div style='font-size:11px;font-weight:500;letter-spacing:2px;
            color:#999;text-transform:uppercase;margin-bottom:8px'>
    AI Assistant
</div>
<div style='font-size:32px;font-weight:600;color:#111;margin-bottom:6px'>
    Ask <span style='color:#2563eb'>anything.</span>
</div>
<div style='font-size:14px;color:#888;margin-bottom:32px'>
    Powered by Gemma 2b — running locally on your machine
</div>
""", unsafe_allow_html=True)

# ── Input ─────────────────────────────────────────────────
input_text = st.text_input(
    "Your question",
    placeholder="e.g. What is machine learning?"
)
ask_btn = st.button("Send →")

# ── Output ────────────────────────────────────────────────
if ask_btn and input_text:
    with st.spinner("Thinking..."):
        response = get_response(input_text)

    st.markdown(f"""
        <div class="answer-card">
            <span class="answer-dot"></span>
            <span class="answer-label">Response</span>
            <div class="answer-text">{response}</div>
        </div>
    """, unsafe_allow_html=True)

elif ask_btn and not input_text:
    st.warning("Please enter a question.")

# ── Footer ────────────────────────────────────────────────
st.markdown("""
    <div class="footer">LangChain · Ollama · Streamlit</div>
""", unsafe_allow_html=True)