import os
import time

from pub_bili import *
from db import *

a=[]
b=["BV1Az4y1D7rD"]
c=[]
d=[]
num=1
start=0
end=0
wait_time=[30,60,300,600]

#def decide_order(item):
    
    
    
    
def item_insert():
    num=0
    flag1=0
    try:
        f_insert=open("insert.txt",mode="r",encoding="utf-8")
        flag1=1
    except Exception:
        flag1=0
    if flag1==1:
        new=f_insert.readlines()
        f_insert.close()
        os.remove("insert.txt")
        for item in new:
            if item[-1]=='\n':
                new_item=item[0:-1]
            b.append(new_item)
            #c[item]=2
            num=num+1
            
while(end>=start):
    item_insert()
    if start==end:
        for item in b:
            a.append(item)
            end=end+1
            #c[item]=1
    #print("Test")
    insert_bhi(video_now_infor(a[start]))       
    print(a[start])
    time.sleep(30/num)
    ##Wait :分优先级爬取 不同优先级 不同时间间隔
    start=start+1