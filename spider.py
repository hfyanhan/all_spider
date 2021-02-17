import os,sys
import time
import threading

from func import *

from pub_zhihu import *

input_flag=0
yon_flag=1

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


#映射函数
order_translate={
    1:bhi,
    2:brh,
    3:zht

} 
#执行次数
order_num={
    1:"No",
    2:"1",
    3:"1",
    }

def order_insert(file_name="insert.txt",flag=1):
    global order_end,input_flag
    flag1=0
    try:
        f_insert=open(file_name,mode="r",encoding="utf-8")
        flag1=1
    except Exception:
        flag1=0
    if flag1==1:
        if input_flag==1:
            return 
        if flag==0:
            input_flag=1
        new=f_insert.readlines()
        f_insert.close()
        if flag==1:    
            os.remove(file_name)
        for item in new:
            new_item=item
            if item[-1]=='\n':
                new_item=item[0:-1]
            
            order_list.append(new_item)
            order_end=order_end+1
            b.append(True)
            order_times.append(0)
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
    if len(sys.argv)==3 and sys.argv[1]=='-s':
        yon_flag=0
        order_insert(file_name=sys.argv[2],flag=yon_flag)
    else:
        order_insert(flag=yon_flag)
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
    time.sleep(1)
    ##Wait :分优先级爬取 不同优先级 不同时间间隔
    start=start+1