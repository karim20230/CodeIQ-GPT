from utils.openai_utils import get_ai_response

def explain_code(user_input: str) -> str:
    prompt = f"Explain this code:\n{user_input}"
    return get_ai_response(prompt)
