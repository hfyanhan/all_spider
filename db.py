import sqlite3
from pub_database import *


def cer_bili():
    video_history={
     'id':'int',
     'bid':'text',
     'time':'text',
     'view':'int',
     'like':'int',
     'coin':'int',
     'favorite':'int',
     'share':'int',
     'danmaku':'int',
     'reply':'int',
     'P_Key':'id'
    }
    rank_history_new={'id':'int',
                  'bid':'text',
                  'time':'text',
                  'from_part':'char(5)',
                  'content':'blob',
                  'P_Key':'id'
    }
    cre_table("bili.db",rank_history_new,"rank_history_new")
def insert_bhi(data):
    cre=sqlite3.connect("bili.db")
    item=data
    item.append(checkhan(cre,"video_history")+1)
    t=cre.cursor()
    t.execute("insert into video_history(bid,view,danmaku,like,coin,favorite,reply,share,time,id)values(?,?,?,?,?,?,?,?,?,?)",item)
    cre.commit()
#cer_bili()