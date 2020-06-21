import telebot
import requests
import datetime

bot = telebot.TeleBot('1002520824:AAEmXpouzu4369NpQLNB9KJ4lQAgD_qYBpg')

url = 'http://api.openweathermap.org/data/2.5/weather'


@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.from_user.id, f'Hello, {message.from_user.username}!')
    bot.send_sticker(message.from_user.id, 'CAACAgIAAxkBAAL2S17vdWUPr2B9EtbyQOTUwnZtZPuWAAJLAAO6wJUFe8p7D7jj6JwaBA')


@bot.message_handler(content_types=['text'])
def handle_text(message):
    try:
        r = requests.get(url, params={
                             'q': message.text,
                             'type': 'like',
                             'units': 'metric',
                             'lang': 'en',
                             'APPID': '0225976b474881be5f367aa4860a6af1'})
        data = r.json()

        time = str(datetime.datetime.now())

        forecast = \
f"""
{data['name']} &#127961:
&#160&#160&#160&#160&#160• <b>Date:</b> {time[:time.index(' ')]}
&#160&#160&#160&#160&#160• <b>Weather description:</b> {data['weather'][0]['description']}
&#160&#160&#160&#160&#160• <b>Temperature:</b> {data['main']['temp']} ℃
&#160&#160&#160&#160&#160• <b>Humidity:</b> {data['main']['humidity']} mm
"""
        bot.send_message(message.from_user.id, forecast, parse_mode='html')

    except Exception:
        bot.send_message(message.from_user.id, "Sorry, I don't know this city &#128532", parse_mode='html')


bot.polling()


