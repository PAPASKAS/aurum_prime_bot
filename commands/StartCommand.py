from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import Dispatcher, types, Bot
from aiogram.filters.command import Command
from app.requests import async_insert_user, async_db_main


class StartCommand:
    _dp: Dispatcher
    _text: dict[str, tuple[str] | str]
    _bot: Bot

    def __init__(self, dp: Dispatcher, text: dict[str, tuple[str] | str], bot: Bot):
        self._text = text
        self._dp = dp
        self._bot = bot

        @self._dp.message(Command('start'))
        async def start(message: types.Message) -> None:
            await async_db_main()
            await async_insert_user(int(message.from_user.id))

            builder = InlineKeyboardBuilder()
            builder.row(types.InlineKeyboardButton(text=self._text['btn_continue_start'], callback_data='continue_start'))

            await message.answer(text=f'Здравствуй {message.from_user.first_name}!')
            await message.answer_photo(photo=types.FSInputFile('./source/IMG_2272.JPG', 'rb'))
            await message.answer(text=self._text['start_message'], reply_markup=builder.as_markup())

        @self._dp.callback_query(lambda call: call.data == 'continue_start')
        async def continue_start(call: types.CallbackQuery) -> None:
            builder = InlineKeyboardBuilder()
            builder.row(types.InlineKeyboardButton(
                text=self._text['btn_continue_start_2'],
                callback_data='continue_start_2'
            ))
            await call.message.answer_photo(
                photo=types.FSInputFile('./source/photo_5391068376601842198_y.jpg', 'rb'),
                reply_markup=builder.as_markup()
            )

        @self._dp.callback_query(lambda call: call.data == 'continue_start_2')
        async def continue_start_2(call: types.CallbackQuery) -> None:
            await call.message.answer(text='https://youtu.be/YWeY7BGGvYU?si=azbxIAKOQ5Zlv0Zf')
            await call.message.answer(text=self._text['continue_start_2'])
            await call.message.answer(text=self._text['input_sections'])
