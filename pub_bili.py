from funcnetio import *
import json,time
header1={
'Host': "api.bilibili.com",
'sec-ch-ua':'''"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"''',
'sec-ch-ua-mobile': '?0',
'Sec-Fetch-Dest': 'document',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-Site': 'none',
'Sec-Fetch-User': '?1',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
}
headers2={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
	  "Referer": "https://www.bilibili.com/ranking/all/0/0/3"}
category_dic={
	"all": "全站榜",
	"origin": "原创榜",
	"rookie": "新人榜",
        "bangumi":"新番榜",
        "cinema": "影视榜"
}
day_dic = {1: "日排行榜", 3: "三日排行榜", 7: "周排行榜", 30: "月排行榜"}
all_or_origin_dic = {
	0: "全站",
	1: "动画",
	168: "国创相关",
	3: "音乐",
	129: "舞蹈",
	4: "游戏",
	36: "科技",
	188: "数码",
	160: "生活",
	119: "鬼畜",
	155: "时尚",
	5: "娱乐",
	181: "影视",
}
rookie_dic = {
	0: "全站",
	1: "动画",
	3: "音乐",
	129: "舞蹈",
	4: "游戏",
	36: "科技",
	188: "数码",
	160: "生活",
	119: "鬼畜",
	155: "时尚",
	5: "娱乐",
	181: "影视",
}
bangumi_dic = {
	1 :  "番剧",
	4 : "国产动画",
}
cinema_dic = {
	3 : "纪录片",
	2 : "电影" ,
	5 : "电视剧",
}
BaseDict = {
	"all": all_or_origin_dic,
        "origin": all_or_origin_dic,
	"rookie": rookie_dic,
        "bangumi": bangumi_dic,
	"cinema": cinema_dic
}
dic = {
	"all": 1,
	"origin": 2,
	"rookie": 3,
}
def video_now_infor(bid):
    url_video="https://api.bilibili.com/x/web-interface/view?bvid="+bid
    data=json.loads(getc(url_video,5,0,header,{}))
    video=[]
    video.append(bid)
    video.append(data["data"]["stat"]["view"])
    video.append(data["data"]["stat"]["danmaku"])
    video.append(data["data"]["stat"]["like"])
    video.append(data["data"]["stat"]["coin"])
    video.append(data["data"]["stat"]["favorite"])
    video.append(data["data"]["stat"]["reply"])
    video.append(data["data"]["stat"]["share"])
    video.append(str(time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime())))
    return video


def get_url():
    task_list=[]
    for first in ["all","origin","rookie","bangumi","cinema"]:
        for second in BaseDict[first].keys():
            for third in day_dic.keys():
                task={}
                if ((third==1 or third==30) and first in ["bangumi", "cinema"]):
                    continue
                if first in ["bangumi", "cinema"]:
                    url = "https://api.bilibili.com/pgc/web/rank/list?day={}&season_type={}".format(third, second)
                if first in ["all", "origin", "rookie"]:
                    url = "https://api.bilibili.com/x/web-interface/ranking?jsonp=jsonp&rid={}&day={}&type={}&arc_type=0&callback=__jp1".format(second, third, dic[first])
                task["url"]=url
                task["kind"]=BaseDict[first][second]
                task["newor"]=category_dic[first]
                task["last"]=day_dic[third]
                task_list.append(task)
    return task_list
def rank_now():
    task_list = get_url()
    for task in task_list:
        print(task["newor"],task["kind"],task["last"],task["url"])
        task["context"]=getc(task["url"],5,0,header2,{})
        task["time"]=str(time.strftime("%Y-%m-%d",time.localtime()))
        time.sleep(2)
    return task_list