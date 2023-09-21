import logging
import speech_recognition
import os
import sys
import webbrowser
import pyttsx3 as p
from datetime import datetime
import time
import datetime
import random
import pyttsx3
import subprocess
from subprocess import run, Popen, PIPE
import psutil
import telebot
from time import sleep
import requests
import json
from bs4 import BeautifulSoup

good = ['повторите', 'не понял', 'не понимаю', 'что-то не понял, повторите', 'я не понимаю, я не понимаю. Я просто расстворяюсь']

#Weather
city = 'Ваш город или район'
link = f"https://www.google.com/search?q=погода+в+{city}"

headers = {
    "User-Agent" : "Ваш User-Agent"
}

responce = requests.get(link, headers=headers)
print(responce)

f = '<Response [200]>'

soup = BeautifulSoup(responce.text, "html.parser")


# Парсим погоду
temperature = soup.select("#wob_tm")[0].getText()
title = soup.select("#wob_dc")[0].getText()
humidity = soup.select("#wob_hm")[0].getText()
time = soup.select("#wob_dts")[0].getText()
wind = soup.select("#wob_ws")[0].getText()


#Бот
API_TOKEN="Token_bot"
bot = telebot.TeleBot(API_TOKEN)
chat_id = 'chat_id'

#Приветствование бота
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.send_message(chat_id, """\
Hello, I am bot
""")

#Логирование
logging.basicConfig(level=logging.INFO, force=False, filename="py_log.log",
                    format="%(asctime)s %(levelname)s %(message)s")

if str(responce) == str(f):
    logging.info('Подключение к серверам google прошло успешно ' + '(' + str(responce) + ')')
else:
    logging.error('Поключение к серверам google прошло неудачно, не удалось подключится!' + '(' + str(responce) + ')', exc_info=True)

#Настройка микрофона    
def command():
    rec = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print('Bot: ...')
        audio = rec.listen(source)
    try:
        text = rec.recognize_google(audio, language="ru-RU").lower()
        print('Вы:  ' + text[0].upper() + text[1:])
    except speech_recognition.UnknownValueError:
        text = {random.choice(good)}
        print('Bot: ' + text)
        text = command()
    return text

def makeSomething(text):
    if 'открой vk' in text:
        try:
            print('Bot: Открываю сайт vk.')
            webbrowser.open('https://vk.com/feed')
            logging.info(f'Открытие VK прошло успешно:)')
        except:
            logging.error('Произошла ошибка с открытием вк', exc_info=True)
    if 'открой вк' in text:
        try:
            print('Bot: Открываю сайт vk.')
            webbrowser.open('https://vk.com/feed')
            logging.info(f'Открытие ВК прошло успешно:)')
        except:
            logging.error('Произошла ошибка с открытием вк', exc_info=True) 
    elif 'открой youtube' in text:
        try:
            print('Bot: Открываю сайт youtube.')
            webbrowser.open('https://www.youtube.com/')
            logging.info(f'Открытие youtube прошло успешно:)')
        except:
            logging.error('Произошла ошибка с открытием youtube', exc_info=True)
    elif 'давай' in text:
        try:
            print('Bot: До свидания!')
            logging.info(f'Прощание с помощником прошло успешно:)')
            sys.exit()
        except:
            logging.error('Я горе программист, поэтому и не смог решить эту проблему, хотя она не очень то и мешает, НО строка кода номер 62 будет работать всегда, хоть и происходит ошибка:D')
            sys.exit()
    elif 'открой telegram' in text:
        try:
            print('Bot: открываю телеграм')
            os.startfile('C:/Users/name_user/AppData/Roaming/Telegram Desktop/Telegram.exe')
            logging.info(f'Открытие телеграм прошло успешно:)')
        except:
            logging.error('Произошла ошибка с открытием телеграм', exc_info=True)
    elif 'открой dota' in text: 
        try:
            print('Bot: открываю dota2')
            os.startfile('D:/SteamLibrary/steamapps/common/dota 2 beta/game/bin/win64/dota2.exe')
            logging.info(f'превращение в хорошего человека прошло успешно, с любовью DOTA2:)')
        except:
            logging.error('Вам очень повезло или наоборот не повезло, что вы не стали хорошим человеком:D', exc_info=True)
    elif 'открой steam' in text: 
        try:
            print('Bot: открываю steam')
            os.startfile('C:/Program Files (x86)/Steam/steam.exe')
            logging.info(f'Открытие steam прошло успешно:)')
        except:
            logging.error('Произошла ошибка с открытием steam, возможно у вас ошибка с кодом или у steam СНОВА проблемы с серверами', exc_info=True)  
    elif 'открой discord' in text: 
        try:
            print('Bot: открываю discord')
            os.startfile('C:/Users/name_user/AppData/Local/Discord/app-1.0.9016/Discord.exe')
            logging.info(f'Открытие discord прошло успешно:)')
        except:
            logging.error('Произошла ошибка с открытием discord', exc_info=True)
    elif 'какая погода' in text:
        try:
            print('Bot: отправляю погоду в телеграмм')
            bot.send_message(chat_id, f"""\
дата и время: {time}
состояние: {title}
температура: {temperature}С
влажность: {humidity}
ветер: {wind}
""")
            logging.info('Отправка погоды произошла успешно')
        except:
            logging.error('Произошла ошибка с показанием погоды, возможные проблемы: проблема с ботом, проблема с сервером, который предоставляет информацию о погоде, также возможно, что ваш интернет не работает.', exc_info=True)

while True:
    makeSomething(command())
