import re
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from bot.content import HELLO_MESSAGE, ABOUT, GOAL, PATH, MENTOR, PROGRESS, HOBBIES, PROJECTS, GITHUB
from bot.keyboards import hello_message_keyboard, back_to_hello_message_keyboard, skip_comment_keyboard
from bot.states import BetterCallAdill
from bot.ai_client import get_ai_response

router = Router()

@router.message(Command("start"))
async def hello_command(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        HELLO_MESSAGE,
        reply_markup = hello_message_keyboard(),
        parse_mode="HTML"
    )

@router.callback_query(F.data == "back")
async def back_to_menu(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.edit_text(
        HELLO_MESSAGE,
        reply_markup = hello_message_keyboard(),
        parse_mode="HTML"
    )
    await callback.answer()

@router.callback_query(F.data == "about")
async def about_me_command(callback: CallbackQuery):
    await callback.message.edit_text(
        ABOUT,
        reply_markup = back_to_hello_message_keyboard(),
        parse_mode = "HTML"
    )
    await callback.answer()

@router.callback_query(F.data == "goal")
async def goal_command(callback: CallbackQuery):
    await callback.message.edit_text(
        GOAL,
        reply_markup = back_to_hello_message_keyboard(),
        parse_mode = "HTML"
    )
    await callback.answer()

@router.callback_query(F.data == "path")
async def path_command(callback: CallbackQuery):
    await callback.message.edit_text(
        PATH,
        reply_markup = back_to_hello_message_keyboard(),
        parse_mode = "HTML"
    )
    await callback.answer()

@router.callback_query(F.data == "mentor")
async def mentor_command(callback: CallbackQuery):
    await callback.message.edit_text(
        MENTOR,
        reply_markup = back_to_hello_message_keyboard(),
        parse_mode = "HTML"
    )
    await callback.answer()

@router.callback_query(F.data == "progress")
async def progress_command(callback: CallbackQuery):
    await callback.message.edit_text(
        PROGRESS,
        reply_markup = back_to_hello_message_keyboard(),
        parse_mode = "HTML"
    )
    await callback.answer()

@router.callback_query(F.data == "hobbies")
async def hobbies_command(callback: CallbackQuery):
    await callback.message.edit_text(
        HOBBIES,
        reply_markup = back_to_hello_message_keyboard(),
        parse_mode = "HTML"
    )
    await callback.answer()

@router.callback_query(F.data == "projects")
async def projects_command(callback: CallbackQuery):
    await callback.message.edit_text(
        PROJECTS,
        reply_markup = back_to_hello_message_keyboard(),
        parse_mode = "HTML"
    )
    await callback.answer()

@router.callback_query(F.data == "github")
async def github_command(callback: CallbackQuery):
    await callback.message.edit_text(
        GITHUB,
        reply_markup = back_to_hello_message_keyboard(),
        parse_mode = "HTML"
    )
    await callback.answer()

@router.callback_query(F.data == "leave_contact")
async def start_fsm(callback: CallbackQuery, state: FSMContext):
    await state.set_state(BetterCallAdill.waiting_for_contact)
    await callback.message.edit_text(
        "Пожалуйста, отправь свой юзернейм в Telegram (начиная с @) или ссылку на свой профиль:",
        reply_markup = back_to_hello_message_keyboard()
    )
    await callback.answer()

@router.message(BetterCallAdill.waiting_for_contact)
async def process_contact(message: Message, state: FSMContext):
    contact = message.text.strip()
    if re.match(r"^(@[a-zA-Z0-9_]{5,32}|(https?://)?(t\.me|telegram\.me)/[a-zA-Z0-9_]{5,32})$", contact):
        await state.update_data(user_contact=contact)
        await state.set_state(BetterCallAdill.waiting_for_comment)
        await message.answer(
            "Контакт записан! Напиши комментарий к твоему обращению (или нажми кнопку ниже, чтобы пропустить):",
            reply_markup=skip_comment_keyboard()
        )
    else:
        await message.answer(
            "Некорректный формат. Пожалуйста, введи валидный никнейм через @ или ссылку на профиль Telegram:"
        )

async def send_lead_to_admin(message: Message, state: FSMContext, comment: str = "Не указан"):
    user_data = await state.get_data()
    contact = user_data.get("user_contact")
    
    username = f"@{message.from_user.username}" if message.from_user.username else "Нет юзернейма"
    user_id = message.from_user.id
    full_name = message.from_user.full_name

    admin_text = (
        "🔔 <b>Новая заявка в боте!</b>\n\n"
        f"👤 <b>Имя:</b> {full_name}\n"
        f"🆔 <b>ID:</b> <code>{user_id}</code>\n"
        f"🌐 <b>Текущий профиль:</b> {username}\n"
        f"📞 <b>Оставленный контакт:</b> {contact}\n"
        f"💬 <b>Комментарий:</b> {comment}"
    )

    await message.bot.send_message(
        chat_id=config.ADMIN_ID, 
        text=admin_text, 
        parse_mode="HTML"
    )
    
    await state.clear()
    await message.answer(
        "Спасибо! Данные успешно отправлены Адилю. Он свяжется с тобой в ближайшее время.",
        reply_markup=back_to_hello_message_keyboard()
    )

@router.callback_query(BetterCallAdill.waiting_for_comment, F.data == "skip_comment")
async def skip_comment(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete()
    await send_lead_to_admin(callback.message, state, comment="Пропущен")
    await callback.answer()

@router.message(BetterCallAdill.waiting_for_comment)
async def process_comment(message: Message, state: FSMContext):
    comment_text = message.text.strip()
    await send_lead_to_admin(message, state, comment=comment_text)

@router.message(F.text)
async def chat_with_ai(message: Message):
    await message.bot.send_chat_action(chat_id=message.chat.id, action="typing")
    ai_response = await get_ai_response(message.text)
    await message.answer(ai_response)
