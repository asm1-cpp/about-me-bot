from aiogram.utils.keyboard import InlineKeyboardBuilder

def hello_message_keyboard():
    builder = InlineKeyboardBuilder()

    blocks = {
        "about":"Про меня", 
        "goal":"Моя цель", 
        "path":"Как я пришел в IT",
        "mentor":"Мой ментор",
        "progress":"Точка А -> Точка Б",
        "hobbies":"Хобби и интересы",
        "porjects":"Мои лучшие работы",
        "github":"Ссылка на GitHub"
    }

    callback = [
        "about",
        "goal",
        "path",
        "mentor",
        "progress",
        "hobbies",
        "projects",
        "github"
    ]

    for block in callback:
        builder.button(
            text = blocks[block],
            callback_data = block
        )

    builder.adjust(
        2,2,2,2
    )

    builder.as_markup()

def back_to_hello_message_keyboard():
    builder = InlineKeyboardBuilder()

    builder.button(text = "Вернуться в главное меню", callback_data = "back")

    builder.as_markup()
