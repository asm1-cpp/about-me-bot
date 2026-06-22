from aiogram.utils.keyboard import InlineKeyboardBuilder
from bot.content import BUTTONS

def hello_message_keyboard():
    builder = InlineKeyboardBuilder()

    blocks = BUTTONS

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
