#!/usr/bin/env python3
#toptenprogrammingL.py: Target => https://www.tiobe.com/tiobe-index/

import requests
import time
from bs4 import BeautifulSoup


data = dict()
headers = ['Programming Language','Rating', 'Change']
def requestpage():
    page = 'https://www.tiobe.com/tiobe-index/'
    response =  requests.get(page)
    return response

def htmlparser():
    response = requestpage()
    soup     = BeautifulSoup(response.text, "html.parser")
    return soup.findAll('table')[0]


def getdata():
    table           = htmlparser()
    header_year     = table.findAll('th')[0]
    header_year     = str(header_year.get_text().strip())

    for i in range(1,11):
         trow =  table.findAll('tr')[i]
         rank = trow.findAll('td')[0]
         rank = str(rank.get_text().strip())
         data.setdefault(header_year, []).append(rank)
         time.sleep(1)

    for h in range(4, len(table.findAll('th'))+1):
        header_plrc = table.findAll('th')[h-1]
        header_plrc = str(header_plrc.get_text().strip())
        for i in range(1, 11):
            trow        = table.findAll('tr')[i]
            plrc_data   = trow.findAll('td')[h]
            plrc_data   = str(plrc_data.get_text().strip())
            data.setdefault(header_plrc, []).append(plrc_data)
        time.sleep(1)
    return header_year


if __name__ == "__main__":
    year = getdata()
    print("{:<10} {:<25} {:<10} {:<10}".format(year,'Programming Language','Rating', 'Change'))
    for i in range(len(data.get(year))):
        for k, v in data.items():
            text = "{:<26}".format(v[i])
            if k not in ['Programming Language','Rating', 'Change']:
                text = "{:<11}".format(v[i])
            print(text, end="")
        print('\n')
