from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os

from config import MODEL_NAME, TEMPERATURE

# Load environment variables
load_dotenv()

# Create a single LLM instance
_llm = ChatGroq(
    model=MODEL_NAME,
    temperature=TEMPERATURE,
    api_key=os.getenv("GROQ_API_KEY"),
)

def get_llm():
    """
    Returns the configured LLM instance.
    """
    return _llm