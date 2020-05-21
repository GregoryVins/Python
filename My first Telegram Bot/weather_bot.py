#!/usr/bin/env python
# -*- coding: utf-8 -*-

import telebot
import requests
from bs4 import BeautifulSoup

TOKEN = '<API key from BotFather>'

bot = telebot.TeleBot(TOKEN)

USERS = {}
THXLIST = ['thank you', 'thx', 'спасибо', 'спс', 'сенкс', 'сенкью', '+']


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Теперь ты можешь просто написать в чат:\n'
                                      'крипта - чтобы узнать курс ТОП 10 криптовалют на текущий момент\n'
                                      'коронавирус - чтобы узнать статистику по РФ на текущий день\n'
                                      '(название города) - без скобок, конечно же. Расскажу о погоде за окном\n')


@bot.message_handler(content_types=['text'])
def get_weather(message):
    try:
        if message.text.lower() == 'коронавирус':
            URL = 'https://yandex.ru/web-maps/covid19?ll=39.103769%2C55.219698&z=7'
            response = requests.get(URL)
            soup = BeautifulSoup(response.text, 'html.parser')
            number_data = soup.findAll('div', {'class': 'covid-stat-view__item-value'})

            result = []
            for i in range(len(number_data)):
                if number_data[i].find(class_='covid-stat-view__item-value') is None:
                    spam = (f'{number_data[i].text}')
                    result.append(spam)
            bot.send_message(message.chat.id, f'Заражений в РФ: {result[0]}\nНовых за последний день: {result[1]}\n'
                                              f'Выздоровлений: {result[2]}\nСмертей: {result[3]}')

        elif message.text.lower() == "крипта":
            URL = 'https://coinmarketcap.com/'
            response = requests.get(URL)
            soup = BeautifulSoup(''.join(response.text), 'html.parser')

            DATA = soup.find_all('span', {'class': 'sc-12ja2s9-0 gRrpzm'})
            name_data = soup.find_all('div', {'class': 'cmc-table__column-name sc-1kxikfi-0 eTVhdN'})
            price_data = soup.find_all('td', {'class': 'cmc-table__cell cmc-table__cell--sortable cmc-table__cell--'
                                                       'right cmc-table__cell--sort-by__price'})
            cap = []
            names = []
            result = []

            for i in range(5):
                if DATA[i].find(class_='cmc-link') is not None:
                    cap.append(DATA[i].text)
                if name_data[i].find(class_='cmc-link') is not None:
                    names.append(name_data[i].text)
                if price_data[i].find(
                        class_='cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--'
                               'sort-by__price') is None:
                    result.append(price_data[i].text)
            clean = []
            i = 0
            while i != len(cap):
                temp = ''
                for el in cap[i]:
                    if el not in '\xa0':
                        temp += el
                clean.append(temp)
                i += 1
            clean = clean[2:]

            bot.send_message(message.chat.id, f'{clean[0]}\n{clean[1]}\n{clean[2]}\n'
                                              f'{names[0]} - {result[0]}\n{names[1]} - {result[1]}\n{names[2]} - '
                                              f'{result[2]}\n{names[3]} - {result[3]}\n{names[4]} - {result[4]}')

        city = message.text.lower()
        URL = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=d5dedfe4c255d3b7703929d0ca3a79a6'
        result = requests.get(URL)
        DATA = result.json()

        bot.send_message(message.chat.id,
                         f"{DATA['name']} {round((DATA['main']['temp']) - 273.15, 1)}C° {DATA['weather'][0]['main']}, {DATA['weather'][0]['description']}\n"
                         f"Влажность {DATA['main']['humidity']}%, cкорость ветра {DATA['wind']['speed']} м/c")
    except Exception:
        pass

    try:
        if message.text.lower() in THXLIST:
            if message.reply_to_message.from_user.id != message.from_user.id:
                if message.reply_to_message.from_user.id in USERS:
                    USERS[message.reply_to_message.from_user.id] += 1
                else:
                    USERS[message.reply_to_message.from_user.id] = 1
            else:
                bot.reply_to(message, 'Благодари себя в другом месте')
    except Exception as error:
        print('Ошибка функции рейтинга "Спасибо". Ошибка:', error)

    try:
        if message.text == 'репутация'.lower():
            bot.reply_to(message, f'Вам сказали спасибо {USERS[message.from_user.id]} раз(а)')
            bot.delete_message(message.chat.id, message.message_id)
    except Exception as error:
        print(f'Ошибка вывода репутации: {error}')

    try:
        if message.text.lower() in ['кто?', 'кто']:
            bot.reply_to(message, 'Т Ы !!!')
            with open('param-pam.jpg', 'rb')as photo:
                bot.send_photo(chat_id=message.chat.id, photo=photo)
    except Exception as error:
        print(f'Ошибка КТО? ТЫ!: {error}')


bot.polling(none_stop=True)
