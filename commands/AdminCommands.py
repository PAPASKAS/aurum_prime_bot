import os

from sqlalchemy import ScalarResult
from aiogram import Dispatcher, types, Bot
from aiogram.filters.command import Command
from app.requests import async_select_users


class AdminCommands:
    _bot: Bot
    _dp: Dispatcher
    _text: dict[str, tuple[str] | str]

    def __init__(self, _dp: Dispatcher, _text: dict[str, tuple[str] | str], _bot: Bot):
        self._bot = _bot
        self._text = _text
        self._dp = _dp

        @self._dp.message(Command('admin'))
        async def admin(message: types.Message) -> None:
            if int(message.from_user.id) == int(os.getenv('ADMIN_ID')):
                markup = types.InlineKeyboardMarkup(resize_keyboard=True, inline_keyboard=[
                    [types.InlineKeyboardButton(text="Рассылка", callback_data='newsletter')],
                ])
                await message.answer('Вы вошли в панель админа', reply_markup=markup)

            @self._dp.callback_query(lambda call: call.data == 'newsletter')
            async def newsletter(call: types.CallbackQuery) -> None:
                await message.answer(self._text['admin_newsletter_1'])

        @self._dp.message(Command('admin_newsletter'))
        async def admin_newsletter(message: types.Message) -> None:
            if int(message.from_user.id) == int(os.getenv('ADMIN_ID')):
                msg = message.text[17:]
                if msg:
                    users: ScalarResult = await async_select_users()
                    for user in users.fetchall():
                        await self._bot.send_message(user.tg_id, msg)
                    await message.answer('Рассылка завершена')
