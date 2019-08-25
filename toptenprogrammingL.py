#!usr/bin/env python3
#toptenprogrammingL.py: Target => https://www.tiobe.com/tiobe-index/

import requests
import urllib.request
import time
from tabulate import tabulate
from bs4 import BeautifulSoup


data = dict()

def requestpage():

    page = 'https://www.tiobe.com/tiobe-index/'
    response =  requests.get(page)
    print(response)
    return response

def htmlparser():
    response = requestpage()
    soup     = BeautifulSoup(response.text, "html.parser")
    return soup.findAll('table')[0]


def getdata():
    table           = htmlparser()
    header_year     = str(table.findAll('th')[0]).translate({ord(i):None for i in "<th></th>"})

    for i in range(1,11):
         trow =  table.findAll('tr')[i]
         rank = str(trow.findAll('td')[0]).translate({ord(i):None for i in "<td></td>"})
         
         data.setdefault(header_year, []).append(rank)
         time.sleep(1)

    for h in range(3, len(table.findAll('th'))):
        
        header_plrc = str(table.findAll('th')[h]).translate({ord(i):None for i in "<th></th>"}) 
        for i in range(1, 11):
            trow        = table.findAll('tr')[i]
            plrc_data   = str(trow.findAll('td')[h]).translate({ord(i):None for i in "<td></td>"})
            data.setdefault(header_plrc, []).append(plrc_data)
        time.sleep(1)
    return header_year

if __name__ == "__main__":
    year = getdata()

    print("{:<25} {:<25} {:<25} {:<25}".format(year,'Programming Language','Rating','Change'))
    
    for i in range(len(data.get(year))):
        for v in data.keys():
            key = data.get(v)
            print("{:<26}".format(key[i]), end = "")
        print("\n")
