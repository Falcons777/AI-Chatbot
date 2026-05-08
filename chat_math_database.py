import re

def solve_math_expression(text):
    # Heq hapësirat e tepërta
    text = text.replace(" ", "")

    # Kthen formatet shqip në symbole matematike
    text = text.replace("plus", "+")
    text = text.replace("minus", "-")
    text = text.replace("shumezim", "*")
    text = text.replace("pjestim", "/")

    # Lejon vetëm numra dhe operatorë
    if re.fullmatch(r"[0-9+\-*/.]+", text):
        try:
            return eval(text, {"__builtins__": {}}, {})
        except (SyntaxError, ZeroDivisionError, TypeError, ValueError):
            return None

    return None
