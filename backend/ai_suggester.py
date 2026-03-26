# from langchain_groq import ChatGroq
# from dotenv import load_dotenv
# from langchain_core.prompts import PromptTemplate
# load_dotenv()

# model = ChatGroq(model="llama-3.1-8b-instant")

# code_string = """
# def calculate_sum(a,b):
#     result = a + b
#     if result > 10:
#         print("Greater than 10")
#     else:
#         print("Less than or equal to 10")
#     return result
# """
# prompt = PromptTemplate(input_variables=["code_string"], template= """You are an experienced coding teacher, so generate the suggestions based on the given code for \n" \
# "the student. Also, not just give the suggestion but tell that why you are suggesting this for eg. if you are suggesting something \n" \
# "to remove then explain that why to remove. \n" \
# "In the suggestion explain the error the code have like the time complexity, space complexity, \n
# also error like naming convention as per pep8 guidelines (for eg: Variables and functions → snake_case and Classes → PascalCase) \n
# and etc. \n" \
# "Code: {code_string} """)

# def get_ai_suggestions(code_string):
#     formatted_promt = prompt.format(code_string=code_string)
#     result = model.invoke(formatted_promt)
#     print(result.content)

# get_ai_suggestions(code_string)
    


import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatGroq(
    model_name="llama-3.1-8b-instant",
    groq_api_key=os.getenv("GROQ_API_KEY")
)

prompt_template = PromptTemplate(
    input_variables=["code_string"],
    template=
 """You are an experienced coding teacher, so generate the suggestions based on the given code for \n" \
# "the student. Also, not just give the suggestion but tell that why you are suggesting this for eg. if you are suggesting something \n" \
# "to remove then explain that why to remove. \n" \
# "In the suggestion explain the error the code have like the time complexity, space complexity, \n
# also error like naming convention as per pep8 guidelines (for eg: Variables and functions → snake_case and Classes → PascalCase) \n
# and etc. \n" \
# "Code: {code_string} """)

def get_ai_suggestion(code_string):
    formatted_prompt = prompt_template.format(code_string=code_string)
    result = model.invoke(formatted_prompt)
    return result.content


if __name__ == "__main__":
    code = "print('Hello')"
    print(get_ai_suggestion(code))