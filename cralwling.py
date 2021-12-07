import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome('./chromedriver')
driver.get('https://www.cryptocompare.com/coins/list/USD/1')
sleep(1)
content = BeautifulSoup(driver.page_source, 'html.parser')
coin = content.findAll('i', {'class': "ng-binding"})
coin_list = []

for i in range(len(coin)):
    title = coin[i].get_text().strip()
    coin_list.append(title)


def write_txt(list, fname, sep):
    file = open(fname, 'w')
    coinstr = ''

    for a in list:
        coinstr = coinstr + str(a) + sep
    coinstr = coinstr.rstrip(sep)  # 마지막 sep빼기
    file.writelines(coinstr)  # 한 라인씩 저장

    file.close()
    print('finished')


write_txt(list=coin_list, fname='coinlist.txt', sep=',')
driver.quit()
