import os
import json
from groq import AsyncGroq
import config
from bot.history_json import save_history, JSON_FILE
from bot.content import system_prompt

client = AsyncGroq(
    api_key=config.API_KEY
)

def load_context_from_json():
    if not os.path.exists(JSON_FILE):
        return []
    with open(JSON_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except (json.JSONDecodeError, KeyError):
            return []

async def get_ai_response(user_message: str) -> str:
    save_history(role="user", text=user_message)
    history = load_context_from_json()

    messages = [{"role": "system", "content": system_prompt}]
    for msg in history:
        role = "assistant" if msg["role"] == "model" else msg["role"]
        messages.append({"role": role, "content": msg["text"]})

    try:
        response = await client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0.3
        )
        ai_text = response.choices[0].message.content
        save_history(role="model", text=ai_text)
        return ai_text
    except Exception as e:
        return f"Ошибка при запросе к Groq: {e}"
