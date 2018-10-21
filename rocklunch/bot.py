# -*- coding: utf-8 -*-

import requests
import datetime

    
link = 'https://launchlibrary.net/1.4/launch'
params = {'startdate': datetime.date.today(), 'limit': 1000}
r = requests.get(link, params = params)
print(r.url)
#print(r.json())




