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
        "github",
        "leave_contact"
    ]

    for block in callback:
        if block in blocks:
            text = blocks[block]
        elif block == "leave_contact":
            text = "Оставить контакт"
        else:
            text = block

        builder.button(
            text = text,
            callback_data = block
        )

    builder.adjust(2, 2, 2, 2, 1)
    return builder.as_markup()

def back_to_hello_message_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text = "Вернуться в главное меню", callback_data = "back")
    return builder.as_markup()

def skip_comment_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="Пропустить ➡️", callback_data="skip_comment")
    return builder.as_markup()
