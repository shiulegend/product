# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 20:26:11 2023

@author: shiul
"""
products = []

while True:
    name = input ('請輸入商品名稱: ')
    if name == 'q':
        break
    price = input ('請輸入商品價錢: ')
    # item = []
    # item.append(name)
    # item.append(price)
    item = [name , price]
    products.append(item)
print (products)

for p in products:
    print(p)