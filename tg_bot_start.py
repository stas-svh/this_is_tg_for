
import telebot
import webbrowser
import random
from telebot import types

bot = telebot.TeleBot('9259607967:AAH_Gx5zblkMZ-ZG-TIuE6tCK3pFaTKlcwk')

quotes = [
    'Цытата: Как говорил один фелосов, люди не пешки, скибиди пельмешки',
    'Цытата: Левый-правый боковой - мне два бургера родной',
    'Цытата: Дают-бери, не дают, укради',
    'Цытата: Путь к величию далек, путь до холодильника ближе',
    'Цытата: Если море было водкой я бы стал подводной лодкой',
    'Цытата: Одна ошибка и ты ошибся',
    'Цытата: Зима не лето - арбуз не котлета',
    'Цытата: Слово не птичка - скибиди яичко',
    'Цытата: Жизнь одна, стендоф два, оливер три'
]



@bot.message_handler(commands=['minigames'])
def mini(message):
    button = types.InlineKeyboardMarkup()
    coin = types.InlineKeyboardButton('Монеточка', callback_data='coin')
    dice = types.InlineKeyboardButton('Кидання кубика', callback_data='dice')
    button.add(coin, dice)
    bot.send_message(message.chat.id, 'Вебери гру:', reply_markup=button)


@bot.callback_query_handler(func=lambda call: True)
def games(call):
    if call.data == 'coin':
        result = random.choice(['Орел', "Решка"])
        bot.edit_message_text(f'Випало: {result}', call.message.chat.id, call.message.message_id)
    elif call.data == 'dice':
        result = random.randint(1, 6)
        bot.edit_message_text(f'Випало: {result}', call.message.chat.id, call.message.message_id)





    bot.answer_callback_query(call.id)


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('перейти на сайт GPT ', url='https://chatgpt.com/')
    markup.row(btn1)

    bot.reply_to(message, '👍', reply_markup=markup)



@bot.message_handler(commands=['youtube', 'watch'])
def site(message):
    markup = types.InlineKeyboardMarkup()
    youbtn1 = types.InlineKeyboardButton('перейти на ютуб', url='https://youtube.com/')
    tiktok1 = types.InlineKeyboardButton('перейти на тикток', url='https://www.tiktok.com/')
    markup.row(youbtn1, tiktok1)
    bot.send_message(message.chat.id, 'перейти на ютуб и тикток:', reply_markup=markup)


@bot.message_handler(commands=['quote'])
def quote(message):
    random_quote = random.choice(quotes)
    bot.send_message(message.chat.id, random_quote)


@bot.message_handler(commands=['start', 'hello'])
def main(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Перейти на сайт Python')
    btn2 = types.KeyboardButton('Перейти на сайт PyCharm')
    markup.row(btn1, btn2)
    bot.send_message(message.chat.id, f'<b>Привіт, {message.from_user.first_name} {message.from_user.last_name}</b>, це перше повідомлення зроблене в цьому боті, цей бот зроблений на пайтон', parse_mode='HTML', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)

def on_click(message):
    if message.text == 'Перейти на сайт Python':
        bot.send_message(message.chat.id, 'This function not working right now')
    elif message.text == 'Перейти на сайт PyCharm':
        bot.send_message(message.chat.id, 'This function not working right now')





@bot.message_handler()
def info(message):
    if message.text.lower() == 'привіт':
        bot.send_message(message.chat.id, f'<b>Привіт, {message.from_user.first_name} {message.from_user.last_name}</b>, це перше повідомлення зроблене в цьому боті', parse_mode='HTML')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id} ')

bot.polling(none_stop=True)
