import sqlite3


def push_database(item,dbfile,table="main"):
    a=1
    #DO:提交至数据库
    #item 字典
    cre=sqlite3.connect(dbfile)
    q=cre.cursor()
    cstr="insert into "+table+"("
    num=0
    values=[]
    for key in item.keys():
        num=num+1   
        cstr=cstr+key+","
        values.append(item[key])
    cstr=cstr[0:-1]+") Values("
    for i in range(1,num+1):
        cstr=cstr+"?,"
    cstr=cstr[0:-1]+");"
    q.execute(cstr,values)
    cre.commit()
    cre.close()
def cre_table(db_name,dic,table_name="main"):
    #dic 字典
    cre=sqlite3.connect(db_name)
    q=cre.cursor()
    cstr="create table "+table_name+"("
    for key in dic.keys():
        if key=="P_Key":
            continue
        cstr=cstr+key+' '+dic[key]
        if dic['P_Key']==key:
            cstr=cstr+" PRIMARY KEY"
        cstr=cstr+','
    cstr=cstr[0:-1]+");"
    q.execute(cstr)
def table_item_name(db_name,table_name):#表的行数 )
    cre=sqlite3.connect(db_name)
    s="select count(*) from "
    s=s+table_name
    oute=cre.execute(s)
    for date in oute:
        d=date[0]
    return d
def item_search(db_name,table_name,search_data,search_word,return_value="number",output_order=[]):#数据库名 表名 待查数据 字段名 返回值 字段顺序
    #查询表中记录(精确查询)
    if return_value=="details" and output_order==[]:
        print("OwnError:No output_order")
        return False
    d=[]
    datsq=[]
    datsq.append(search_data)
    cre=sqlite3.connect(db_name)
    s="select "
    for word in output_order:
        s=s+word+" "
    s=s+"from "+table_name+" where "+search_word+"=?"
    oute=cre.execute(s,datsq)
    #print(s)
    sum=0
    for date in oute:
        sum=sum+1
        d.append(date)
    if d==[] :
        return 0
    if return_value=="number":
        return sum
    if return_value=="details":
        ans=[]
        for item in d:
            temp_item={}
            i=0
            for word in output_order:
                temp_item[word]=item[i]
                i=i+1
            ans.append(temp_item)
        return ans
