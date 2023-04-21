# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 20:26:11 2023

@author: shiul
"""
products = []

#讀取檔案
with open('product.csv' , 'r' , encoding= 'utf-8') as f:
    for line in f:
        # s = line.strip().split(',')
        # print(s)
        
        if '商品,價格' in line:
            continue
        
        name , price = line.strip().split(',')
        products.append([name , price])
print (products)
      

while True:
    name = input ('請輸入商品名稱: ')
    if name == 'q':
        break
    price = input ('請輸入商品價錢: ')
    prict = int(price)
    # item = []
    # item.append(name)
    # item.append(price)
    item = [name , price]
    products.append(item)
print (products)

for p in products:
    print(p)
    
for p in products:
    print(p[0] , '的價格是' , p[1])
    
#實際寫入電腦檔案 字串合併時，price是數字先轉為文字
with open('product.csv' , 'w' , encoding= 'utf-8') as f :
    f.write('商品,價格\n')
    for p in products:
        f.write(p[0] + ',' + str(p[1]) + '\n')