from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def start_keyboard():
    markup = InlineKeyboardMarkup()
    questionnaire_button = InlineKeyboardButton(
        "Start quiz",
        callback_data="start_questionnaire"
    )
    markup.add(questionnaire_button)
    return markup


async def questionnaire_one_keyboard():
    markup = InlineKeyboardMarkup()
    yes_button = InlineKeyboardButton(
        "Yes!!",
        callback_data="yes_start"
    )
    no_button = InlineKeyboardButton(
        "No!",
        callback_data="no_start"
    )
    markup.add(yes_button)
    markup.add(no_button)
    return markup

