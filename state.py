import reflex as rx
from typing import List, Dict
from backend.code_analyzer import analyze_code_pipeline
from backend.ai_suggester import get_ai_suggestion


class State(rx.State):
    code: str = ""
    errors: List[str] = []
    ai_suggestions: str = ""
    history: List[Dict] = []
    loading: bool = False

    # 🔹 Help Chat
    chat_input: str = ""
    chat_output: str = ""

    # ✅ Setter for input
    def set_chat_input(self, value: str):
        self.chat_input = value

    # 🔹 ANALYZE CODE
    def analyze(self):
        self.loading = True

        result = analyze_code_pipeline(self.code)

        self.errors = result.get("errors", [])

        # ✅ SAFE FORMATTING (NO '*' replace)
        formatted = result.get("ai_suggestions", "")
        formatted = formatted.replace("###", "\n\n###")

        self.ai_suggestions = formatted

        self.history.append({
            "code": self.code,
            "errors": self.errors,
            "ai": self.ai_suggestions
        })

        self.history = self.history[-10:]
        self.loading = False

    # 🔹 AI HELP
    def ask_ai(self):
        if not self.chat_input.strip():
            self.chat_output = "Please enter a question"
            return

        response = get_ai_suggestion(self.chat_input)

        # ✅ SAFE FORMATTING
        formatted = response.replace("###", "\n\n###")

        self.chat_output = formatted