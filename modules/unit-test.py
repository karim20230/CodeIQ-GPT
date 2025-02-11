from utils.openai_utils import get_ai_response

def generate_unit_tests(user_input: str) -> str:
    prompt = f"Generate unit tests for the following code:\n{user_input}"
    return get_ai_response(prompt)
