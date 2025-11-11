import streamlit as st
import requests

from app.config.settings import settings
from app.common.logger import get_logger
from app.common.custom_exception import CustomException

logger = get_logger(__name__)

st.set_page_config(page_title="Multi AI agent", layout ="centered")
st.title("Multi AI agent using Groq and Travily")

system_prompt = st.text_area("Define the AI Agent:", height=70)
selected_model = st.selectbox("Select your AI model:", settings.ALLOWED_MODEL_NAMES)

allow_web_search = st.checkbox("Allow web search:")
user_query = st.text_area("Enter your query:", height=150)

API_URL = "http://127.0.0.1:9999/chat"

if st.button("Ask Agent:") and user_query.strip():
  payload = {
    "model_name": selected_model,
    "system_prompt": system_prompt,
    "allow_search": allow_web_search,
    "messages": [user_query],
  }

  try:
    logger.info("Sending request to backend")
    response = requests.post(API_URL, json=payload)
    
    if response.status_code == 200:
      agent_response = response.json().get("response", "")
      logger.info("Successfully got response from backend")
    
      st.subheader("Agent response")
      st.markdown(agent_response.replace("\n", "<br>"), unsafe_allow_html=True)
    
    else:
      logger.error("Backend error")
      st.error("Error at backend")
  
  except Exception as e:
    logger.error(f"Error at backend {e}")
    st.error("Failed at backend")

