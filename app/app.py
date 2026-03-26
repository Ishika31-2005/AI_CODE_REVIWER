






import reflex as rx
from state import State

# ---------- NAVBAR ----------
def navbar():
    return rx.hstack(
        rx.text(" AI Code Reviewer", font_weight="bold", font_size="20px"),
        rx.spacer(),
        rx.link("Home", href="/"),
        rx.link("Analyzer", href="/analyzer"),
        rx.link("History", href="/history"),
        rx.link("Help", href="/help"),
        rx.link("About", href="/about"),
        padding="15px 30px",
        bg="#0d1117",
        color="white",
        border_bottom="1px solid #30363d",
        position="fixed",
        top="0",
        width="100%",
        z_index="1000"
    )


# ---------- HOME ----------
def home():
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                rx.heading("AI Code Reviewer 💻", size="9"),
                rx.text("Analyze your Python code using AI", color="gray"),
                spacing="5",
                align="center"
            ),
            height="100vh"
        ),
        bg="#0d1117",
        color="white"
    )


# ---------- ANALYZER ----------
def analyzer():
    return rx.box(
        navbar(),

        rx.hstack(
            # LEFT SIDE
            rx.box(
                rx.heading("Code Editor", color="white"),

             
                rx.text(
                    "Write your Python code here...",
                    color="#9ca3af",
                    font_size="14px",
                    margin_bottom="5px"
                ),

                rx.text_area(
                    on_change=State.set_code,
                    height="450px",
                    width="100%",
                    bg="#161b22",
                    color="white",
                    border="1px solid #30363d",
                    border_radius="10px",
                    padding="12px",
                    font_size="15px",
                ),

                rx.button(
                    "🔍 Analyze Code",
                    on_click=State.analyze,
                    color_scheme="blue",
                    margin_top="12px"
                ),

                width="60%",
                padding="20px"
            ),

            # RIGHT SIDE
            rx.box(
                rx.heading("Output", color="white"),

                rx.text("Errors:", weight="bold"),
                rx.box(
                    rx.foreach(
                        State.errors,
                        lambda err: rx.text(err, color="red")
                    ),
                    padding="10px",
                    bg="#0d1117",
                    border="1px solid #30363d",
                    border_radius="8px",
                    margin_bottom="10px"
                ),

                rx.divider(),

                rx.text("AI Suggestions:", weight="bold"),

                rx.box(
                    rx.text(
                        State.ai_suggestions,
                        white_space="pre-wrap"
                    ),
                    bg="#0d1117",
                    padding="15px",
                    border="1px solid #30363d",
                    border_radius="10px",
                    height="400px",
                    overflow="auto"
                ),

                width="40%",
                bg="#161b22",
                padding="20px",
                border="1px solid #30363d",
                border_radius="10px"
            ),

            padding_top="80px",
            width="100%"
        ),

        bg="#0d1117",
        color="white",
        min_height="100vh"
    )


# ---------- HISTORY ----------
def history():
    return rx.box(
        navbar(),

        rx.vstack(
            rx.heading("History"),

            rx.foreach(
                State.history,
                lambda item: rx.box(
                    rx.text("Code:", weight="bold"),
                    rx.text(item["code"]),
                    rx.text("Errors:", weight="bold"),
                    rx.text(str(item["errors"])),
                    rx.text("AI:", weight="bold"),
                    rx.text(item["ai"], white_space="pre-wrap"),
                    bg="#161b22",
                    padding="15px",
                    border="1px solid #30363d",
                    border_radius="10px"
                )
            ),

            spacing="4",
            padding_top="80px"
        ),

        bg="#0d1117",
        color="white",
        min_height="100vh"
    )


# ---------- HELP ----------
def help_page():
    return rx.box(
        navbar(),

        rx.center(
            rx.vstack(
                rx.heading("AI Help 🤖", size="8", color="white"),

              
                rx.text(
                    "Ask your programming question here...",
                    color="#9ca3af",
                    font_size="14px",
                    margin_bottom="5px"
                ),

                rx.text_area(
                    on_change=State.set_chat_input,
                    width="600px",
                    height="150px",
                    bg="#161b22",
                    color="white",
                    border="1px solid #30363d",
                    border_radius="8px",
                    padding="10px",
                    font_size="14px",
                ),

                rx.button(
                    "Send",
                    on_click=State.ask_ai,
                    color_scheme="blue"
                ),

                rx.box(
                    rx.text(
                        State.chat_output,
                        white_space="pre-wrap"
                    ),
                    bg="#0d1117",
                    padding="12px",
                    border="1px solid #30363d",
                    border_radius="8px",
                    width="600px",
                    height="250px",
                    overflow="auto"
                ),

                spacing="4",
                align="center"
            ),
            height="100vh"
        ),

        bg="#0d1117",
        color="white"
    )


# ---------- ABOUT ----------
def about():
    return rx.box(
        navbar(),

        rx.center(
            rx.box(
                rx.vstack(
                    rx.heading("About AI Code Reviewer"),

                    rx.text(
                        "AI Code Reviewer analyzes Python code and provides smart suggestions.",
                        color="gray"
                    ),

                    rx.divider(),

                    rx.text("• Code analysis using AST"),
                    rx.text("• AI suggestions"),
                    rx.text("• Error detection"),
                    rx.text("• History tracking"),

                    rx.divider(),

                    rx.text("Built using Reflex + LangChain + Groq"),

                ),
                bg="#161b22",
                padding="30px",
                border_radius="12px",
                width="500px"
            ),
            height="100vh"
        ),

        bg="#0d1117",
        color="white"
    )


# ---------- APP ----------
app = rx.App()

app.add_page(home, route="/")
app.add_page(analyzer, route="/analyzer")
app.add_page(history, route="/history")
app.add_page(help_page, route="/help")
app.add_page(about, route="/about")