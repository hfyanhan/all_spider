import re,zipfile,os


def is_exist(file_name):
	try:
		f=open(file_name,mode="r",encoding="gb2312")
	except IOError:
	   return 0
	f.close()
	return 1

def write_read_file(file_name,method="read",text):#将字符串写入文件或读取文件 写入内容 名称 读或写 文件后缀
	num=str(num)
	if method=="read":
		f=open(num,mode="r",encoding="utf-8")
		return_text=f.read()
		f.close()
		return return_text
	f=open(num,mode="a",encoding="utf-8")
	f.write(text)
	f.close()
	return "Successfully!"