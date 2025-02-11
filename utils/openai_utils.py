import os
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
chat_model = ChatOpenAI(model="gpt-4", api_key=OPENAI_API_KEY)

def get_ai_response(prompt: str) -> str:
    try:

        response = chat_model([HumanMessage(content=prompt)])
        return response.content
    except Exception as e:
        return f"Error: {str(e)}"
