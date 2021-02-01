import sqlite3

def checkhan(cre,tabn):#表的行数 参数(数据库连接，表名(str))
    s="select count(*) from "
    s=s+tabn
    oute=cre.execute(s)
    for date in oute:
        d=date[0]
    return d
def checkjl(cre,table,wils,wild):#数据库连接 表名 待查数据  列名
    #查询表中记录(精确查询)
    d=[]
    datsq=[]
    datsq.append(wils)
    s="select * from "+table+" where "+wild+"=?"
    oute=cre.execute(s,datsq)
    sum=0
    for date in oute:
        sum=sum+1
        d.append(date[0])
    if d==[] :
        return 0
    return sum
#cre=sqlite3.connect("score2019.db")
#print(checkjl(cre,"luyang","118A+","yuwen"))