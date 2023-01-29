#!/usr/bin/env python

import datetime
import requests
from bs4 import BeautifulSoup

datetime_object = datetime.datetime.now()
full_month_name = datetime_object.strftime("%B")
day_of_month = datetime_object.strftime("%d")

# Making a GET request
r = requests.get('https://last-day-on-earth-survival.fandom.com/wiki/Bunker_Alfa')

# check status code for response received
# success code - 200
if r.status_code == 200:

    # Parsing the HTML
    soup = BeautifulSoup(r.content, 'html.parser')

    s = soup.find('div', class_='mw-parser-output')

    lines = s.find_all('p')

    for line in lines:
        # Look at only lines with correct month
        if (line.text).startswith(full_month_name):
            # Split multi lined <p>
            for li in (line.text).split('\n'):
                # Search for lines with day
                if day_of_month in li:
                    day = li.split()
                    # Only show correct line
                    if day_of_month in day[1]:
                        #print(day[2])
                        print(li)
