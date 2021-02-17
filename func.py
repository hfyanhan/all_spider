from pub_bili import *
from pub_zhihu import *

def bhi(bid):
    data=bili_video_now_infor(bid)
    data['id']=table_item_name("bili.db","video_history")+1
    push_database(data,"bili.db",table="video_history")
def brh():
    data=bili_rank_now()
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
