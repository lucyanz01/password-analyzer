import re

CRITERIA = {
    "length": 8,
    "uppercase": r"[A-Z]",
    "lowercase": r"[a-z]",
    "numbers": r"\d",
    "special_chars": r"[!@#$%^&*(),.?\":{}|<>]"
}

def password_analyzer(password: str):
    score = 0
    feedback = []

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Too short")

    for name, pattern in list(CRITERIA.items())[1:]:
        if re.search(pattern, password):
            score += 1
        else:
            feedback.append(f"Missing: {name}")

    strength = "weak" if score <= 2 else "medium" if score <= 4 else "strong"

    return {
        "score": score,
        "strength": strength,
        "missing": feedback
    }