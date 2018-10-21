# -*- coding: utf-8 -*-

import requests
import datetime
from telegram.ext import Updater, CommandHandler


updater = Updater(token='747634004:AAHdq92vQW0pQiwyAfiw7x0Gfzus9zH9FNw')

dispatcher = updater.dispatcher

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

    




link = 'https://launchlibrary.net/1.4/launch'
params = {'startdate': datetime.date.today(), 'limit': 1000}
r = requests.get(link, params = params)
print(r.url)
#print(r.json())




