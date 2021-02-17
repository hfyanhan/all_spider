from pub_net import *
import json,time
import header
from pub_database import *

all_dic = {
	0: "全站a",
    1: "动画b",
	168: "国创相关c",
	3: "音乐d",
	129: "舞蹈e",
	4: "游戏f",
	36: "科技g",
	188: "数码h",
	160: "生活i",
	119: "鬼畜j",
	155: "时尚k",
	5: "娱乐l",
	181: "影视m",
    217:"动物圈n",
    211:"美食o"
}


dic = {
	"all": 1,
	"origin": 2,
	"rookie": 3,
}
def bili_video_now_infor(bid):
    url_video="http://api.bilibili.com/x/web-interface/view?bvid="+bid
    data=json.loads(get_post(url=url_video,header=header.header1))
    video={}
    video['bid']=bid
    video['view']=data["data"]["stat"]["view"]
    video['danmaku']=data["data"]["stat"]["danmaku"]
    video['like']=data["data"]["stat"]["like"]
    video['coin']=data["data"]["stat"]["coin"]
    video['favorite']=data["data"]["stat"]["favorite"]
    video['reply']=data["data"]["stat"]["reply"]
    video['share']=data["data"]["stat"]["share"]
    video['time']=str(time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime()))
    return video


def get_url():
    task_list=[]
    for first in all_dic.keys():
        task={}
        url = "https://api.bilibili.com/x/web-interface/ranking/v2?rid={}&type=all".format(first)
        task["url"]=url
        task["kind"]=all_dic[first]
        task_list.append(task)
    task_rookie={
        'url':"https://api.bilibili.com/x/web-interface/ranking/v2?rid=0&type=rookie",
        'kind':'新人榜p'
    }
    task_origin={
        'url':"https://api.bilibili.com/x/web-interface/ranking/v2?rid=0&type=origin",
        'kind':'原创榜q'
    }
    task_list.append(task_rookie)
    task_list.append(task_origin)
    return task_list
def bili_rank_now():
    will_del=["aid",'dislike','his_rank','now_rank']
    video_ok={}
    time_now=str(time.strftime("%Y-%m-%d",time.localtime()))
    time_detail=str(time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime()))
    task_list = get_url()
    ans_list={}
    for task in task_list:
        print(task["kind"],task["url"])
        context=get_post(url=task["url"],header=header.header2)
        context=json.loads(context)
        rank=0
        for item in context["data"]["list"]:
            video_ok[item['bvid']]=video_ok.get(item['bvid'],True)
            if video_ok[item['bvid']]:
                video_ok[item['bvid']]=False
                data=item["stat"]
                for word in will_del:
                    data.pop(word)
                data['bid']=item['bvid']
                data['time']=time_detail
                data['id']=table_item_name("bili.db","video_history")+1
                push_database(data,"bili.db",table="video_history")
            ans_list[item['bvid']]=ans_list.get(item['bvid'],{})
            ans_list[item['bvid']]['bid']=item['bvid']
            ans_list[item['bvid']]['time']=time_now
            temp=ans_list[item['bvid']].get('content',b'')
            temp=temp+str.encode(task['kind'][-1])+str.encode(str(rank))
            ans_list[item['bvid']]['content']=temp
            rank=rank+1
        time.sleep(2)
    return ans_list

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
                  'content':'blob',
                  'P_Key':'id'
    }
    cre_table("bili.db",rank_history_new,"rank_history_new")