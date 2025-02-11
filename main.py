import os
import streamlit as st
from modules.code_explanation import explain_code
from modules.code_debugging import debug_code
from modules.code_refactoring import refactor_code
from modules.code_documentation import add_documentation
from modules.code_quality import check_code_quality
from modules.code_security import check_security
from modules.unit_tests import generate_unit_tests

# Load OpenAI API Key (assumes it's set in environment)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Streamlit UI
st.title("💻 AI Code Assistant")
st.write("Enhance your code with AI-powered suggestions!")

# Select Mode: Choose which feature to use
mode = st.selectbox("Select Mode:", ["Explain Code", "Debug Code", "Refactor Code", 
                                     "Add Documentation", "Check Code Quality", 
                                     "Check Security", "Generate Unit Tests"])

# User input: Code to analyze
user_input = st.text_area("Paste your code here:")

if st.button("Submit") and user_input:
    # Call the respective function based on the selected mode
    if mode == "Explain Code":
        st.text_area("AI Explanation:", explain_code(user_input), height=300)
    elif mode == "Debug Code":
        st.text_area("AI Debugging:", debug_code(user_input), height=300)
    elif mode == "Refactor Code":
        st.text_area("AI Refactor:", refactor_code(user_input), height=300)
    elif mode == "Add Documentation":
        st.text_area("AI Documentation:", add_documentation(user_input), height=300)
    elif mode == "Check Code Quality":
        st.text_area("AI Quality Check:", check_code_quality(user_input), height=300)
    elif mode == "Check Security":
        st.text_area("AI Security Check:", check_security(user_input), height=300)
    elif mode == "Generate Unit Tests":
        st.text_area("AI Unit Tests:", generate_unit_tests(user_input), height=300)
