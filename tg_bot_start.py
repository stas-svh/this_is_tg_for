import telebot
import webbrowser


bot = telebot.TeleBot('9259607967:AAH_Gx5zblkMZ-ZG-TIuE6tCK3pFaTKlcwk')

@bot.message_handler(commands=['youtube', 'watch'])
def site(message):
    webbrowser.open('https://www.youtube.com/')



@bot.message_handler(commands=['start', 'hello'])
def main(message):
    bot.send_message(message.chat.id, f'<b>Привіт, {message.from_user.first_name} {message.from_user.last_name}</b>, це перше повідомлення зроблене в цьому боті', parse_mode='HTML')


@bot.message_handler()
def info(message):
    if message.text.lower() == 'привіт':
        bot.send_message(message.chat.id, f'<b>Привіт, {message.from_user.first_name} {message.from_user.last_name}</b>, це перше повідомлення зроблене в цьому боті', parse_mode='HTML')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id} ')

bot.polling(none_stop=True)