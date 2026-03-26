import ast

def parse_code(code_string):
    """
    Parse Python code and check for syntax errors.
    """

    try:
        ast.parse(code_string)
        return {
            "success": True,
            "message": "No syntax errors found."
        }

    except SyntaxError as e:
        return {
            "success": False,
            "error": {
                "message": f"Syntax Error: {e.msg}",
                "line": e.lineno,
                "offset": e.offset
            }
        }


