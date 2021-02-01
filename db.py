import sqlite3
from funcsq import *


def cer_bili():
    cre=sqlite3.connect("bili.db")
    t=cre.cursor()
    t.execute('''
                CREATE TABLE video_history(
                id int PRIMARY KEY,
                bid text,
                time text,
                view int,
                like int,
                coin int,
                favorite int,
                share int,
                danmaku int,
                reply int);''')
    #t.execute('''
     #          id int PRIMARY KEY,
      #          aid int,
       #         time text,
def insert_bhi(data):
    cre=sqlite3.connect("bili.db")
    item=data
    item.append(checkhan(cre,"video_history")+1)
    t=cre.cursor()
    t.execute("insert into video_history(bid,view,danmaku,like,coin,favorite,reply,share,time,id)values(?,?,?,?,?,?,?,?,?,?)",item)
    cre.commit()
    