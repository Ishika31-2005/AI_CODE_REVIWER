import ast

class AIReviewer(ast.NodeVisitor):
    def __init__(self):
        self.defined = set()
        self.used = set()
        self.findings = []

    def visit_Import(self, node):
        for alias in node.names:
            self.defined.add(alias.name)
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        for alias in node.names:
            self.defined.add(alias.name)
        self.generic_visit(node)

    def visit_FunctionDef(self, node):
        # Function length check
        if hasattr(node, "end_lineno"):
            length = node.end_lineno - node.lineno + 1
            if length > 40:
                self.findings.append(
                    f"Function '{node.name}' is too long ({length} lines)."
                )
        self.generic_visit(node)

    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Store):
            self.defined.add(node.id)
        elif isinstance(node.ctx, ast.Load):
            self.used.add(node.id)
        self.generic_visit(node)

    def report_unused(self):
        unused = self.defined - self.used

        for item in unused:
            if item != "print":
                self.findings.append(f"Unused item found: {item}")

        return self.findings


def analyze_code(code_string):
    tree = ast.parse(code_string)
    reviewer = AIReviewer()
    reviewer.visit(tree)
    return reviewer.report_unused()

