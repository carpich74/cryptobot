

import telebot # импортируем библиотеку

from config import keys, TOKEN # импортируем библиотеку
from extensions import ConvertionException, CryptoConverter # импортируем библиотеку


bot = telebot.TeleBot(TOKEN)




@bot.message_handler(commands=['start', 'help']) #
def start(message: telebot.types.Message):   #
    text = "👋 Привет, я бот-помощник, введите комманду боту в следующем формате: \n<имя валюты> \n<в какую валюту перевести > \n<количество переводимой валюты> \nЧтобы увидеть список всех доступных валют: /values ." # создаем переменную
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])  # создаем обработчик команды
def values(message: telebot.types.Message): # создаем функцию
    text = "Доступные валюты:" # создаем переменную
    for key in keys.keys(): # создаем цикл
        text = '\n'.join((text, key)) # добавляем в переменную
    bot.reply_to(message, text)  # отправляем сообщение пользователю



@bot.message_handler(content_types=['text', ])  # создаем обработчик текста
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ') # создаем переменную
        if len(values) != 3: # создаем условие
            raise ConvertionException('Слишком много параметров.') # создаем исключение

    # if quote == base: # создаем условие
    #     raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}.') # создаем исключение
        quote, base, amount = values  # создаем переменные
        total_base = CryptoConverter.convert(quote, base, amount)

    except ConvertionException as e: # создаем исключение
        bot.reply_to(message, f'Ошибка пользователя.\n{e}') # отправляем сообщение пользователю
    except Exception as e: #создаем исключение
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else: # создаем условие
        text = f'Цена {amount} {quote} в {base} - {total_base}'
        bot .send_message(message.chat.id, text)

  






bot.polling(none_stop=True)  #