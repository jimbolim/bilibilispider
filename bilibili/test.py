import requests
import os

pro = open('proxys.txt','r')
res = open('right.txt','w')
test = pro.readlines()
for te in test:
    for i in range(20):
        try:
            a = requests.get('http://api.bilibili.com/archive_stat/stat?aid='+str(i),proxies={'http' : 'http://'+te}, timeout=0.5)
            print(a)
        except:
            print(te)
            break
    else:
        res.write('http://'+te)
pro.close()
res.close()
