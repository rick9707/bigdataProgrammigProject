import pandas as pd
from pandas import DataFrame
import os
import csv
import glob
import time
a = 0
for a in range(3):
    file_list = glob.glob(f'./trash/{a}/*.csv')
    if(a == 0):
        price = pd.read_csv('./semi/result1_171.csv')
    else:

        i = 0
        for item in file_list:
            start = time.time()
            print(item)
            item = str(item.replace("\\", "/"))
            name = item[13:-8]
            data = pd.read_csv(item, names=['name', 'USD', 'KOR'])
            data = data[['name', 'KOR']].rename(
                columns={'name': 'name', 'KOR': name})

            price = pd.merge(price, data, on="name")
            print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
            print(i)
            i = i + 1


filename = f'./semi/result1_17.csv'
price.to_csv(filename, mode='w')
