import ast
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load API key from .env
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize Groq model
llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model="llama-3.1-8b-instant"
)

def parse_code(code_string):
    """
    Parse python code and check for syntax errors.
    """

    try:
        tree = ast.parse(code_string)
        return {"success": True, "code": code_string}

    except SyntaxError as e:
        return {
            "success": False,
            "error": {
                "message": f"Syntax Error: {str(e)}"
            }
        }

def get_ai_feedback(code):
    prompt = f"Analyze this Python code and give improvement suggestions:\n\n{code}"
    response = llm.invoke(prompt)
    return response.content


code_result = parse_code("""
def calculate_sum(a,b):
    result = a+b
    if result>10:
        print("greater than 10")
    else:
        print("less than or equal to 10")
    return result
""")

if code_result["success"]:
    print("Code parsed successfully!\n")
    feedback = get_ai_feedback(code_result["code"])
    print("AI Suggestions:\n")
    print(feedback)
else:
    print(code_result["error"]["message"])

