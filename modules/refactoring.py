from utils.openai_utils import get_ai_response

def refactor_code(user_input: str) -> str:
    prompt = f"Refactor the following code for better readability and performance:\n{user_input}"
    return get_ai_response(prompt)
