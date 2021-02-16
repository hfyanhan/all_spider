from pub_net import *
import json,time
import header
category_dic={
	"all": "全站榜",
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
        "bangumi": bangumi_dic,
	"cinema": cinema_dic
}
dic = {
	"all": 1,
	"origin": 2,
	"rookie": 3,
}
another_dic={'日排行榜':'a',
'三日排行榜':'b',
'周排行榜':'c',
'月排行榜':'d'
}
def video_now_infor(bid):
    url_video="http://api.bilibili.com/x/web-interface/view?bvid="+bid
    data=json.loads(get_post(url=url_video,header=header.header1))
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
    for first in ["all","bangumi","cinema"]:
        for second in BaseDict[first].keys():
            for third in day_dic.keys():
                task={}
                if ((third==1 or third==30) and first in ["bangumi", "cinema"]):
                    continue
                if first in ["bangumi", "cinema"]:
                    continue
                    #url = "https://api.bilibili.com/pgc/web/rank/list?day={}&season_type={}".format(third, second)
                if first in ["all", "origin", "rookie"]:
                    url = "https://api.bilibili.com/x/web-interface/ranking?jsonp=jsonp&rid={}&day={}&type={}&arc_type=0".format(second, third, dic[first])
                task["url"]=url
                task["kind"]=BaseDict[first][second]
                task["newor"]=category_dic[first]
                task["last"]=day_dic[third]
                task_list.append(task)
    return task_list
def rank_now():
    time_now=str(time.strftime("%Y-%m-%d",time.localtime()))
    task_list = get_url()
    ans_list={}
    for task in task_list:
        print(task["newor"],task["kind"],task["last"],task["url"])
        context=get_post(url=task["url"],header=header.header2)
        context=json.loads(context)
        rank=0
        for item in context["data"]["list"]:
            ans_list[item['bvid']]={}
            ans_list[item['bvid']]['bid']=item['bvid']
            ans_list[item['bvid']]['from_part']=task['kind']
            ans_list[item['bvid']]['time']=time_now
            temp=ans_list[item['bvid']].setdefault('content',b'')
            temp=temp+str.encode(another_dic[task['last']])+str.encode(str(rank))
            ans_list[item['bvid']]['content']=temp
            rank=rank+1
        time.sleep(1)
    return ans_list
