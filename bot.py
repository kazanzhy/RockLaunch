# -*- coding: utf-8 -*-

import requests
import datetime as dt
import logging

from telegram.ext import Updater, CommandHandler, Job


def get_launches(num=5):
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



HOST =  '10.100.6.210:5000'

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
updater = Updater(token='')
dispatcher = updater.dispatcher
job_queue = updater.job_queue

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

upcoming_handler = CommandHandler('upcoming', upcoming)
dispatcher.add_handler(upcoming_handler)


updater.start_polling()










