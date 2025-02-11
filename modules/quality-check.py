from utils.openai_utils import get_ai_response

def check_code_quality(user_input: str) -> str:
    prompt = f"Analyze the quality of the following code and suggest improvements:\n{user_input}"
    return get_ai_response(prompt)
