import logging
from aiogram import Bot, Dispatcher, executor, types

from oxfordLookup import getDefinitions
from googletrans import Translator

translator = Translator()

API_TOKEN = '5762793278:AAF8qOxhpeHWbgqqtSHFn6beWEOzYg1zUYc'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Assalomu alaykum!\nMen Oxford English botman!\nFoydalanish yo'riqnomasini ko'rish uchun /help tugmasini bosing")
    
@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("1️⃣Agar siz menga bitta so'z jo'natsangiz, men sizga o'sha so'zning ma'nolarini va audiosini jo'nataman!\n2️⃣Agar menga birorta gap jo'natsangiz, men uni sizga o'zbek tiliga tarjima qilib beraman!")

@dp.message_handler()
async def tarjimon(message: types.Message):
    lang = translator.detect(message.text).lang
    if len(message.text.split()) > 1:
    	dest = 'uz' if lang=='en' else 'en'
    	await message.reply(translator.translate(message.text, dest).text)
    else:
    	if lang == 'en':
    		word_id =message.text
    	else:
    		word_id = translator.translate(message.text, dest = 'en').text
    	
    	lookup = getDefinitions(word_id)	
    	if lookup:
    		await message.reply(f"Word: {word_id} \nDefinitions: \n{lookup['definitions']}")
    		if lookup.get('audio'):
    			await message.reply_voice(lookup['audio'])
    		else:
    			await message.reply("Bunday so'z topilmadi!")
    
    
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)