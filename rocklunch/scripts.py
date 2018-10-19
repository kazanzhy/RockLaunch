# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import json

def parse_nasa():
    link = 'https://www.nasa.gov/api/2/calendar-event/_search'
    date_from = '2018-10-19T00:00:00-04:00'
    date_to = '2028-10-19T00:00:00-04:00'
    q = '(calendar-name:6089 AND event-date.value:[{} TO {}] AND event-date-count:1)'.format(date_from, date_to)
    params = {'size': '100', 'from': '0', 'sort': 'event-date.value', 'q': q}
    r = requests.get(link, params = params)
    events = r.json()['hits']['hits']
    for event in events:
        print(event)
        print()
   

parse_nasa()

#soup = BeautifulSoup(r.text, 'html.parser')
#print(soup)

