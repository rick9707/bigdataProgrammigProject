import pandas as pd
from pandas import DataFrame
import os
import csv
import glob
import time
a = 0

file_list = glob.glob(f'./semi/*.csv')

price = pd.read_csv('./price.csv')

i = 0
for item in file_list:
    start = time.time()

    data = pd.read_csv(item)

    price = pd.merge(price, data)

    print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
    print(i)
    i = i + 1


filename = f'./semi/resultsum.csv'
price.to_csv(filename, mode='w')
