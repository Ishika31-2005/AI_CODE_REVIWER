import ast
from backend.code_parser import parse_code
from backend.error_detector import AIReviewer
from backend.ai_suggester import get_ai_suggestion


def analyze_code_pipeline(code):
    syntax_result = parse_code(code)

    if not syntax_result["success"]:
        return {
            "errors": [syntax_result["error"]["message"]],
            "ai_suggestions": ""
        }

    tree = ast.parse(code)

    reviewer = AIReviewer()
    reviewer.visit(tree)
    findings = reviewer.report_unused()

    ai_suggestion = get_ai_suggestion(code)

    return {
        "errors": findings if findings else ["No issues found"],
        "ai_suggestions": ai_suggestion
    }

import json

   
