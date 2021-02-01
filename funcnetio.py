def isexist(s):
	try:
		f=open(s,mode="r",encoding="gb2312")
	except IOError:
	   return 0
	f.close()
	return 1
def getc(htm,sleept,flag,headers,cookies):#url 失败后等待时间 是否需要重编码 headers cookies
	import requests,time
	while 1:
		der=0
		try:
			r=requests.get(htm,headers=headers,cookies=cookies)
			r.raise_for_status()
			#print(r.status_code)
			if flag==1:
				r.encoding=r.apparent_encoding
		except Exception :
			print("获取Url失败,继续尝试")
			time.sleep(sleept)
			der=3
		if der==0 :
			break
	w=r.text
	return w
def wrhtml(text,num,how,hou):#将查询到的网页写入文件或读取文件 写入内容 名称 读或写 文件后缀
	num=str(num)
	num=num+"."+hou
	if how==2:
		f=open(num,mode="r",encoding="utf-8")
		q=f.read()
		f.close()
		return q
	f=open(num,mode="w",encoding="utf-8")
	f.write(text)
	f.close()
	return "Successfully!"
def realine(f):
	w=[]
	while 1:
		date=f.readline()
		if not date:
			break
		w.append(date[0:len(date)-1])
	print(w)
	return w