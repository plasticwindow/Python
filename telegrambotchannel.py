import telebot
import requests
import weather  # API Token для погоды
from tokenTelegramBot import TelegramToken  # АPI Token Telegram бота


#Телеграм Бог
bot = telebot.TeleBot(TelegramToken)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    mes = message.text.lower()
    if "погода" in mes:
        # Чистим переменную для выгрузки в get API
        mas = mes.replace("погода", "")
        # Чистим
        mas = mas.replace(" ", "")
        respone = requests.get(
            weather.apiurlweather + mas + weather.tokenweather)
        if not respone.status_code == 404:
            kelvin = respone.json()['main']['temp']  # Температура
            country = respone.json()['sys']['country']  # Страна
            # Конвертация из градусов Кельвина в градусы Цельсия
            celsiya = int(kelvin) - int(273)
            celsiya = str(celsiya)
            bot.send_message(message.chat.id, "Температура: "
                             + celsiya
                             + "\nСтрана: "
                             + country
                             )
    else:
        message.text = None


bot.polling(none_stop=True, interval=0)
