from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from bot.content import HELLO_MESSAGE, ABOUT, GOAL, PATH, MENTOR, PROGRESS, HOBBIES, PROJECTS, GITHUB
from bot.keyboards import hello_message_keyboard, back_to_hello_message_keyboard

router = Router()

@router.message(Command("start"))
async def hello_command(message: Message):
    await message.answer(
        HELLO_MESSAGE,
        reply_markup = hello_message_keyboard(),
        parse_mode="HTML"
    )

@router.callback_query(F.data == "about")
async def about_me_command(callback: CallbackQuery):
    await callback.answer(
        ABOUT,
        reply_markup = back_to_hello_message_keyboard(),
        parse_mode = "HTML"
    )

@router.callback_query(F.data == "goal")
async def goal_command(callback: CallbackQuery):
    await callback.answer(
        GOAL,
        reply_markup = back_to_hello_message_keyboard(),
        parse_mode = "HTML"
    )

@router.callback_query(F.data == "path")
async def path_command(callback: CallbackQuery):
    await callback.answer(
        PATH,
        reply_markup = back_to_hello_message_keyboard(),
        parse_mode = "HTML"
    )

@router.callback_query(F.data == "mentor")
async def mentor_command(callback: CallbackQuery):
    await callback.answer(
        MENTOR,
        reply_markup = back_to_hello_message_keyboard(),
        parse_mode = "HTML"
    )

@router.callback_query(F.data == "progress")
async def progress_command(callback: CallbackQuery):
    await callback.answer(
        PROGRESS,
        reply_markup = back_to_hello_message_keyboard(),
        parse_mode = "HTML"
    )

@router.callback_query(F.data == "hobbies")
async def hobbies_command(callback: CallbackQuery):
    await callback.answer(
        HOBBIES,
        reply_markup = back_to_hello_message_keyboard(),
        parse_mode = "HTML"
    )

@router.callback_query(F.data == "projects")
async def projects_command(callback: CallbackQuery):
    await callback.answer(
        PROJECTS,
        reply_markup = back_to_hello_message_keyboard(),
        parse_mode = "HTML"
    )

@router.callback_query(F.data == "github")
async def github_command(callback: CallbackQuery):
    await callback.answer(
        GITHUB,
        reply_markup = back_to_hello_message_keyboard(),
        parse_mode = "HTML"
    )
