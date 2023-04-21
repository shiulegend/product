# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 20:26:11 2023

@author: shiul
"""

#檢核是否有檔案 讀取檔案和return的回傳值
import os

def read_file(filename):
    products = []
  #讀取檔案
    with open(filename , 'r' , encoding= 'utf-8') as f:
      for line in f:
          # s = line.strip().split(',')
          # print(s)
          
          if '商品,價格' in line:
              continue
          
          name , price = line.strip().split(',')
          products.append([name , price])
    return products
      
#讓使用者輸入產品
def user_input(products):
    while True:
        name = input ('請輸入商品名稱: ')
        if name == 'q':
            break
        price = input ('請輸入商品價錢: ')
        price = int(price)
        # item = []
        # item.append(name)
        # item.append(price)
        item = [name , price]
        products.append(item)
    print (products)
    return products

#印出所有商品
def print_products(products):
    for p in products:
        print(p[0] , '的價格是' , p[1])
    
#實際寫入電腦檔案 字串合併時，price是數字先轉為文字
def write_file(filename, products):
    with open(filename , 'w' , encoding= 'utf-8') as f :
        f.write('商品,價格\n')
        for p in products:
            f.write(p[0] + ',' + str(p[1]) + '\n')
   


#主程式流程，先確認檔案再用read_file的function
def main():
    filename = 'product.csv'
    if os.path.isfile(filename):
        print('找到檔案')
        products = read_file(filename)     
    else:
        print('找不到檔案')
     
    
    #傳入products後，加入新的商品再入products
    #function有回傳值，可以存入變數
    products = user_input(products)
    #帶入products參數，避免去functon外的世界拿值
    print_products(products)
    write_file('product.csv', products)
  
#開始主程式
main()