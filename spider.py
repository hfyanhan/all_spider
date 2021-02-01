import os
import time

from pub_bili import *
from db import *

do_list=[]
do_xyz=[]
b=[]
xyz=[]
order_list=[]
order_times=[]
d=[]
start=0
end=0
order_end=0
wait_time=[30,60,300,600]

#def decide_order(item):
    
order_translate={
    1:"bhi",
    2:"brh"


}    
order_num={
    1:"No",
    2:"1"
    
    
    }
order_xyz={
    1:1,
    2:0
    }
def order_insert():
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
            order_list.append(new_item)
            global order_end
            order_end=order_end+1
            b.append(True)
            order_times.append(0)
            if end!=0:
                b[order_end-1]=one_order_process(new_item)
def one_order_process(order,i):
    global order_times,end
    if order_times[i]==0:
        #for j in range(0,order_xyz[order[0]]):
        xyz.append(order.split( )[1:1+len(order.split( ))])   
    order_times[i]=order_times[i]+1
    do_list.append(int(order[0]))
    do_xyz.append(xyz[i])
    end=end+1
    #print(order_times[i])
    if str(order_times[i])==order_num[int(order[0])]:
        return False
    return True
def order_process():
    for i in range(0,order_end):
        #print(b[i])
        if b[i]==True:
            b[i]=one_order_process(order_list[i],i)
            
#for i in range(0,9999):
    
while(end>=start):
    order_insert()
    
    if start==end:
        do_list=[]
        do_xyz=[]
        end=start=0
        order_process()
        if do_list==[]:
            break
           
    if do_list[start]==1:
        insert_bhi(video_now_infor(do_xyz[start][0]))
    if do_list[start]==2:
        insert_rankhis(rank_now())
    out_xyz=""
    for xyz in do_xyz[start]:
        out_xyz=out_xyz+xyz+" "
    print(do_list[start],out_xyz)   
    time.sleep(3)
    ##Wait :分优先级爬取 不同优先级 不同时间间隔
    start=start+1