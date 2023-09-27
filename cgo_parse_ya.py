# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 23:29:05 2023

@author: Bohdan Yailymov
"""

import pandas as pd
from datetime import date

ds = pd.read_html('http://cgo-sreznevskyi.kyiv.ua/uk/diialnist/khimichne-zabrudnennia/sposterezhennia-za-zabrudnenniam-atmosfernoho-povitria-v-mkyievi', encoding = 'utf-8', decimal=",", thousands='.', header=1)
lst = ds
cur = date.today()

number_table = ['3', '5', '7', '20', '21', '22', '22']

for i,adds in zip(number_table,lst):
    df = pd.DataFrame(adds)
    df.to_csv(str(cur)+'-'+str(i)+'-cgo.csv')
    print(str(cur)+'-'+str(i))