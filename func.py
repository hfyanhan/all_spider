from pub_bili import *
from db import *
from pub_zhihu import *

def bhi(data):
    insert_bhi(video_now_infor(data))
def brh():
    data=rank_now()
    for bid in data.keys():
        data[bid]['id']=table_item_name("bili.db","rank_history_new")+1
        push_database(data[bid],"bili.db",table="rank_history_new")
def zht():
    data=zhihu_hot_rank()
    for item in data:
        item['id']=table_item_name("zhihu.db","hot_rank")+1
        push_database(item,"zhihu.db",table="hot_rank")
    data=zhihu_hot_search()
    for item in data:
        item['id']=table_item_name("zhihu.db","hot_search")+1
        push_database(item,"zhihu.db",table="hot_search")
