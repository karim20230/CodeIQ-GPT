from utils.openai_utils import get_ai_response

def add_documentation(user_input: str) -> str:
    prompt = f"Add docstrings and comments to the following code:\n{user_input}"
    return get_ai_response(prompt)
