import random
import os

path = "C:\Questions" #資料夾目錄
files= os.listdir(path) #得到資料夾下的所有檔名稱
s = []
for file in files: #遍歷資料夾
    if not os.path.isdir(file): #判斷是否是資料夾，不是資料夾才開啟
        f = open(path+"/"+file); #開啟檔案
        iter_f = iter(f); #建立迭代器
        text = ""
        for line in iter_f: #遍歷檔案，一行行遍歷，讀取文字
            text = text + line
        s.append(text) #每個檔案的文字存到list中
for i in range(1, 4):
    n = random.randrange(10) + 1
    print('Question ' + str(n), end=".")
    print(s[n-1])
    print('\n=======================================\n')
    response = input()
    while response!='A' and response!='B' and response!='C' and response!='D':
        print('Your format of input is incorrect. It only accept A,B,C and D. Please try again.')
        response = input()
files.clear()