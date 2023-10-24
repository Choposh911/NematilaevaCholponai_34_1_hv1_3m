from aiogram import types, Dispatcher
from config import bot
from keyboards.inline_buttons import questionnaire_one_keyboard



async def start_questionnaire(call: types.CallbackQuery):
    with open("C:/Users/acer/PycharmProjects/choposhssbot/media/areuready.gif", 'rb') as animation:
        await bot.send_animation(
            chat_id=call.message.chat.id,
            animation=animation,
            caption=f"DO YOU WANT TO KNOW YOUR ENGLISH LEVEL?",
            reply_markup=await questionnaire_one_keyboard()
        )


async def yes_answer(call: types.CallbackQuery):
    await  bot.send_message(
        chat_id=call.message.chat.id,
        text=f"LET'S START!"
    )
def register_callback_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(start_questionnaire, lambda call: call.data == "start_questionnaire")
    dp.register_callback_query_handler(yes_answer, lambda call: call.data == "yes_start")
    dp.register_callback_query_handler(no_answer, lambda call: call.data == "no_start")


async def no_answer(call: types.CallbackQuery):
    await  bot.send_message(
        chat_id=call.message.chat.id,
        text=f"OK!"
    )



