from pub_net import  *
from pub_database import *
import json,time

def cre_zhihu():
    hot_search={
    'id':'int',
    'time':'text',
    'word':'text',
    'all_word':'text',
    'P_Key':'id'
    }
    hot_rank={
        'id':'int',
        'P_Key':'id',
        'qid':'int',
        'title':'text',
        'hot':'text',
        'time':'text'
    }
    cre_table("zhihu.db",hot_search,"hot_search")
    cre_table("zhihu.db",hot_rank,"hot_rank")

def zhihu_hot_search():
    time_now=str(time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime()))
    url2="https://www.zhihu.com/api/v3/feed/topstory/hot-lists/total?limit=100&desktop=true"
    url="https://www.zhihu.com/api/v4/search/top_search"
    t=json.loads(get_post(url))
    ans_list=[]
    for item in t['top_search']['words']:
        ans={}
        ans['time']=time_now
        ans['word']=item['query']
        ans['all_word']=item['display_query']
        ans_list.append(ans)
    return ans_list
def zhihu_hot_rank():
    time_now=str(time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime()))
    url="https://www.zhihu.com/api/v3/feed/topstory/hot-lists/total?limit=100&desktop=true"
    t=json.loads(get_post(url))
    ans_list=[]
    for item in t['data']:
        ans={}
        ans['time']=time_now
        ans['title']=item['target']['title']
        ans['qid']=item['target']['id']
        ans['hot']=item['detail_text']
        ans_list.append(ans)
    return ans_list

