# -*- coding: utf-8 -*-

import os
import logging
import datetime as dt

import requests

from telegram.ext import Updater, CommandHandler, Job

from database import session
from config import TOKEN

def get_launches(num=5):
    # Gets next 5 launches
    link = 'https://launchlibrary.net/1.4/launch/next/' + str (num)
    data = requests.get(link).json()
    launches = data['launches']
    return launches


def start(bot, update):
    text = "Hi. I'll inform you about the next launch.\nPress /upcoming to see upcoming rocket launches"
    bot.send_message(chat_id=update.message.chat_id, text=text)


def upcoming(bot, update):
    launches = get_launches()
    for l in launches:
        text = 'Mission: <a href="{}">{}</a>\n'.format(HOST + '/launch/' + str(l['id']), l['name'])
        text += 'Date: <i>{}</i>\n'.format(l['net'])
        text += 'Spaceport: <a href="{}">{}</a>\n'.format(l['location']['pads'][0]['mapURL'], l['location']['pads'][0]['name'])
        text += 'Rocket: <a href="{}">{}</a>\n'.format(l['rocket']['wikiURL'], l['rocket']['name'])
        text += 'LSP: <a href="{}">{}</a>\n'.format(l['lsp']['wikiURL'], l['lsp']['name'])
        text += 'Webcast: ' + ''.join(['<a href="' + url + '">' + url + '</a>\n' for url in l['vidURLs']])
        bot.send_message(chat_id=update.message.chat_id, text=text, parse_mode='html', disable_web_page_preview=True)



logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

upcoming_handler = CommandHandler('upcoming', upcoming)
dispatcher.add_handler(upcoming_handler)


updater.start_polling(poll_interval=0.0, timeout=10, clean=False, bootstrap_retries=-1, read_latency=2.0, allowed_updates=None)
#updater.start_webhook(listen='127.0.0.1', port=80, url_path='', cert=None, key=None, clean=False, bootstrap_retries=0, webhook_url=None, allowed_updates=None)








