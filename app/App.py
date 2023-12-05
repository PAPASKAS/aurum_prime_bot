import asyncio
import logging
import os

import Text
from commands import StartCommand, SectionsCommands, AdminCommands
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types


class App:
    _bot: Bot
    _dp: Dispatcher
    _text: dict[str, tuple[str] | str]
    _commands: set = set()

    def __init__(self):
        load_dotenv()
        self._bot = Bot(token=os.getenv('BOT_TOKEN'), parse_mode='HTML')
        self._dp = Dispatcher(bot=self._bot)
        self._text = Text.Text().text

        self._commands.add(StartCommand.StartCommand)
        self._commands.add(SectionsCommands.SectionsCommands)
        self._commands.add(AdminCommands.AdminCommands)

        for command in self._commands:
            command(self._dp, self._text, self._bot)

        @self._dp.message()
        async def echo_message(message: types.Message) -> None:
            await message.reply(text='Я тебя не понимаю')

    async def start(self) -> None:
        logging.basicConfig(level=logging.INFO)
        await self._dp.start_polling(self._bot)


if __name__ == '__main__':
    asyncio.run(App().start())
