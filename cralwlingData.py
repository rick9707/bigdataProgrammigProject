import requests
import pandas as pd
import csv
import time
import threading


def getapi1():
    timestr = time.strftime("%Y%m%d-%H%M%S")
    print(timestr)
    filename = './data/18/1_'+timestr+'.csv'

    file = open('./coinlist.txt', 'r')
    lines = file.readlines()
    file.close()
    coins = lines[0].split(',')
    payload_coin = str(coins).replace("'", "").replace(" ", "")
    payload_coin1 = payload_coin[1:297]

    apiKey = "99b2692c85cb818a0486659df97d1890f71437aea79fe736978ed8f76c7a37d5"

    url = "https://min-api.cryptocompare.com/data/pricemulti"

    payload = {
        "fsyms": {payload_coin1},
        "tsyms": {"USD", "KRW"}
    }

    headers = {
        "authorization": "Apikey " + apiKey
    }

    result1 = requests.get(url, headers=headers, params=payload).json()
    csv_file = open(filename, 'w', encoding='utf-8')

    for c in coins[:67]:

        money = result1[c]
        KRW = money["KRW"]
        USD = money["USD"]
        price_list = [c, KRW, USD]
        writer = csv.writer(csv_file)
        writer.writerow(price_list)

    csv_file.close


getapi1()
