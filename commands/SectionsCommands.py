from aiogram import Dispatcher, types, Bot
from aiogram.filters.command import Command


class SectionsCommands:
    _bot: Bot
    _dp: Dispatcher
    _text: dict[str, tuple[str] | str]

    def __init__(self, _dp: Dispatcher, _text: dict[str, tuple[str] | str], _bot: Bot):
        self._bot = _bot
        self._text = _text
        self._dp = _dp

        @self._dp.message(Command('sections'))
        async def sections(message: types.Message) -> None:
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
                [types.KeyboardButton(text=self._text['btn_sections_1'])],
                [types.KeyboardButton(text=self._text['btn_sections_2'])],
                [types.KeyboardButton(text=self._text['btn_sections_3'])],
                [types.KeyboardButton(text=self._text['btn_sections_4'])],
                [
                    types.KeyboardButton(text=self._text['btn_sections_5']),
                    types.KeyboardButton(text=self._text['btn_sections_6'])
                ],
                [types.KeyboardButton(text=self._text['btn_sections_7'])],
                [types.KeyboardButton(text=self._text['btn_sections_8'])],
                [types.KeyboardButton(text=self._text['btn_sections_9'])],
            ])
            await message.answer(self._text['sections_title'], reply_markup=keyboard)

        # yandere router
        @self._dp.message()
        async def router(message: types.Message) -> None:
            if message.text == self._text['btn_sections_1']:
                await self.section_1(message)
            elif message.text == self._text['btn_sections_2']:
                await self.section_2(message)
            elif message.text == self._text['btn_sections_3']:
                await self.section_3(message)
            elif message.text == self._text['btn_sections_4']:
                await self.section_4(message)
            elif message.text == self._text['btn_sections_5']:
                await self.section_5(message)
            elif message.text == self._text['btn_sections_6']:
                await self.section_6(message)
            elif message.text == self._text['btn_sections_7']:
                await self.section_7(message)
            elif message.text == self._text['btn_sections_8']:
                await self.section_8(message)
            elif message.text == self._text['btn_sections_9']:
                await self.section_9(message)

    async def section_1(self, message: types.Message) -> None:
        await message.answer(text='https://youtu.be/8OPR6ue3t3A?si=AtZEJeXtOgD6UmlF')
        await message.answer(text=self._text['section_1'])

    async def section_2(self, message: types.Message) -> None:
        await message.answer(text='https://youtu.be/-tASxlOFBI0?si=ffDoA7rl0oreYghn')
        await message.answer(text=self._text['section_2'])

    async def section_3(self, message: types.Message) -> None:
        await message.answer_photo(
            photo=types.FSInputFile('./source/photo_5391068376601842213_y.jpg', 'rb'),
            caption=self._text['section_3.1']
        )
        await message.answer(text='https://youtu.be/-WPRtNjKw3w?si=b6DdaemLpu2EDFuL')
        await message.answer(text=self._text['section_3.2'])

    async def section_4(self, message: types.Message) -> None:
        await message.answer(text='https://youtu.be/8dI7njjjP0g?si=8fWF0mO66aepDjs0')
        await message.answer(text=self._text['section_4'])

    async def section_5(self, message: types.Message) -> None:
        await message.answer(text=self._text['section_5'])

    async def section_6(self, message: types.Message) -> None:
        await message.answer(text=self._text['section_6'])

    async def section_7(self, message: types.Message) -> None:
        await message.answer(text=self._text['section_7.1'])
        await message.answer_photo(
            photo=types.FSInputFile('./source/photo_5224349711950002499_y.jpg', 'rb'),
            caption=self._text['section_7.2']
        )

    async def section_8(self, message: types.Message) -> None:
        await message.answer(text='https://youtu.be/Sxz6iLw2EU4?si=FGe_W_p--nRXabge')
        await message.answer(text=self._text['section_8'])

    async def section_9(self, message: types.Message) -> None:
        await message.answer(text='https://youtu.be/vOfhL7QuNQ4?si=TjinZTE1d59ZKPmx')
        await message.answer(text=self._text['section_9.1'])
        await message.answer(text='https://youtu.be/uNZdQYKWNCY?si=vlCIpZD5dy7E-DI4')
        await message.answer(text=self._text['section_9.2'])
        await message.answer_photo(
            photo=types.FSInputFile('./source/photo_5391068376601842338_y.jpg', 'rb'),
            caption=self._text['section_9.3']
        )
