from utils.openai_utils import get_ai_response

def check_security(user_input: str) -> str:
    prompt = f"Check the following code for security vulnerabilities:\n{user_input}"
    return get_ai_response(prompt)
