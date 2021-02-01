import sqlite3
from funcsq import *


def cer_bili():
    cre=sqlite3.connect("bili.db")
    t=cre.cursor()
    #t.execute('''
     #           CREATE TABLE video_history(
      #          id int PRIMARY KEY,
       #         bid text,
        #        time text,
         #       view int,
          #      like int,
           #     coin int,
            #    favorite int,
             #   share int,
              #  danmaku int,
               # reply int);''')
    t.execute('''CREATE TABLE rank_history(
               id int PRIMARY KEY,
                kind text,
                time text,
                newor text,
                last text,
                context text);      
       ''')
def insert_bhi(data):
    cre=sqlite3.connect("bili.db")
    item=data
    item.append(checkhan(cre,"video_history")+1)
    t=cre.cursor()
    t.execute("insert into video_history(bid,view,danmaku,like,coin,favorite,reply,share,time,id)values(?,?,?,?,?,?,?,?,?,?)",item)
    cre.commit()
def insert_rankhis(data):
    for task in data:
        item=[]
        for string in ["context","time","newor","kind","last"]:
            item.append(task[string])
        cre=sqlite3.connect("bili.db")
        item.append(checkhan(cre,"rank_history")+1)
        t=cre.cursor()
        t.execute("insert into rank_history(context,time,newor,kind,last,id)")
    cre.commit()
#cer_bili()    