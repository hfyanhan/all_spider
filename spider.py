import os
import sys
import threading
import time

from func import *

local_order_flag=0

do_list=[]
do_xyz=[]
order_insert_do_list_flag=[]
order_xyz=[]
order_list=[]
order_times=[]
do_start=0
do_end=0
order_end=0
wait_time=[30,60,300,600]



#def decide_order(item):


#映射函数
order_translate={
    1:bhi,
    2:brh,
    3:zht

} 
#执行次数
order_num={
    1:"NoLimit",
    2:"1",
    3:"1",
    }


def split_xyz(order):
    return order.split()[1:1+len(order.split())]

def order_insert(file_name="insert.txt"):
    global order_end,order_xyz,local_order_flag
    have_insert_flag=0
    try:
        f_insert=open(file_name,mode="r",encoding="utf-8")
        have_insert_flag=1
    except Exception:
        have_insert_flag=0
    if have_insert_flag==1:
        new_order_list=f_insert.readlines()
        f_insert.close()
        if local_order_flag==0:
            os.remove(file_name)
        for new_order in new_order_list:
            if new_order[-1]=='\n':
                new_order=new_order[0:-1]
            
            order_list.append(new_order)
            order_xyz.append(split_xyz(new_order))
            order_end=order_end+1
            order_insert_do_list_flag.append(True)
            order_times.append(0)

def one_order_process(order,i):
    global order_times,do_end,order_xyz,do_xyz,do_list
        
    order_times[i]=order_times[i]+1
    do_list.append(int(order[0]))
    do_xyz.append(order_xyz[i])
    do_end=do_end+1
    
    if str(order_times[i])==order_num[int(order[0])]:
        return False
    return True

def order_process():
    for i in range(0,order_end):
        if order_insert_do_list_flag[i]==True:
            order_insert_do_list_flag[i]=one_order_process(order_list[i],i)


if len(sys.argv)==3 and sys.argv[1]=='-s':
    local_order_flag=1
    order_insert(file_name=sys.argv[2])
while(do_end>=do_start):
    if local_order_flag==0:
        order_insert()
    if do_start==do_end:
        do_list=[]
        do_xyz=[]
        do_end=do_start=0
        order_process()
        if do_list==[]:
            break    
    t=threading.Thread(target=order_translate[do_list[do_start]],args=do_xyz[do_start])
    t.start()
    t.join()
    
    out_xyz=""
    for xyz_i in do_xyz[do_start]:
        out_xyz=out_xyz+xyz_i+" "
    print(do_list[do_start],out_xyz)
    time.sleep(30)
    ##Wait :分优先级爬取 不同优先级 不同时间间隔
    do_start=do_start+1
