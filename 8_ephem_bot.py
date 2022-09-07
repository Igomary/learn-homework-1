import ephem
from datetime import datetime
"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn',
        'password': 'python'
    }
}


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(text)

def check_planet(update, context):
    print('Вызван /planet')
    user_text = update.message.text.split(' ')
    planet_name = user_text[len(user_text)-1].capitalize()
    date_now = datetime.today().strftime('%Y/%m/%d')
    
    try:
        planet = getattr(ephem,planet_name)
        constel = ephem.constellation(planet(date_now)) 
        print(f'Привет, планета {planet_name} сейчас находится в созвездии {constel}')

        update.message.reply_text(f'Привет, планета {planet_name} сейчас находится в созвездии {constel}')
    except AttributeError:
        update.message.reply_text('введите правильное название планеты')  


def main():
    mybot = Updater("КЛЮЧ, КОТОРЫЙ НАМ ВЫДАЛ BotFather", request_kwargs=PROXY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler("planet", check_planet))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
