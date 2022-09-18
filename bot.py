from aiogram import Bot, types, Dispatcher, executor
from main import get_video

bot = Bot(token='5730783891:AAEB3_8UTdBbeI35kWo0MQSbITw_nVge1Lo')
dp = Dispatcher(bot)

@dp.message_handler()
async def send_mp3(message: types.Message):
    name_video = get_video(url=message.text)
    doc = open(name_video, 'rb')
    await message.reply_document(doc)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
