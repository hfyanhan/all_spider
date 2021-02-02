import os
import time
import threading
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
    
   
order_num={
    1:"No",
    2:"1"
    
    
    }
order_xyz={
    1:1,
    2:0
    }

def bhi(data):
    insert_bhi(video_now_infor(data))
def brh():
    insert_rankhis(rank_now())



order_translate={
    1:bhi,
    2:brh

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
    global order_times,end,xyz,do_xyz,do_list
    if order_times[i]==0:
        xyz.append(order.split( )[1:1+len(order.split( ))])
    order_times[i]=order_times[i]+1
    do_list.append(int(order[0]))
    do_xyz.append(xyz[i])
    end=end+1
    
    if str(order_times[i])==order_num[int(order[0])]:
        return False
    return True
def order_process():
    for i in range(0,order_end):
        #print(b[i])
        if b[i]==True:
            b[i]=one_order_process(order_list[i],i)
            
while(end>=start):
    order_insert()
    
    if start==end:
        do_list=[]
        do_xyz=[]
        end=start=0
        order_process()
        if do_list==[]:
            break    
    t=threading.Thread(target=order_translate[do_list[start]],args=do_xyz[start])
    t.start()
    t.join()
    
    out_xyz=""
    for xyz_i in do_xyz[start]:
        out_xyz=out_xyz+xyz_i+" "
    print(do_list[start],out_xyz)   
    time.sleep(30)
    ##Wait :分优先级爬取 不同优先级 不同时间间隔
    start=start+1