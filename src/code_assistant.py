from fastapi import FastAPI
from pydantic import BaseModel
import os
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

# Load OpenAI API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
chat_model = ChatOpenAI(model="gpt-4", api_key=OPENAI_API_KEY)

# Create FastAPI app
app = FastAPI()

class CodeRequest(BaseModel):
    mode: str
    language: str
    code: str

@app.post("/analyze_code")
async def analyze_code(request: CodeRequest):
    prompt = f"{request.mode} this {request.language} code:\n{request.code}"
    response = chat_model([HumanMessage(content=prompt)])
    return {"response": response.content}

# Run API server: `uvicorn code_assistant:app --host 0.0.0.0 --port 8000`
