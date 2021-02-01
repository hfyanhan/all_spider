while(1):
    a=input()
    a=a+"\n"
    f_insert=open("insert.txt",mode="a",encoding="utf-8")
    f_insert.write(a)
    f_insert.close()