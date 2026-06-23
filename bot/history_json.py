import json
import os

JSON_FILE = "context.json"

def save_history(role, text, max_messages = 5):
    if not os.path.exists(JSON_FILE):
        history = []
    else:
        with open(JSON_FILE, "r", encoding="utf-8") as f:
            try:
                history = json.load(f)
            except json.JSONDecodeError:
                history = []

    history.append({
        "role": role,
        "text": text
    })

    if len(history) > max_messages:
        history = history[-max_messages:]

    with open(JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=4)

    return history
