from funcnetio import *
import json,time
header={
'Host': "api.bilibili.com",
'sec-ch-ua':'''"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"''',
#'Cookie': "buvid3=B0D9BECB-D695-414B-846A-B2EDA4C7857640772infoc; LIVE_BUVID=AUTO8515593048657300; pgv_pvi=152973312; sid=b53gif2j; blackside_state=1; CURRENT_FNVAL=80; DedeUserID=447571231; DedeUserID__ckMd5=6bf16ff15c0a360b; SESSDATA=724a5e12%2C1617290904%2Cd85c1*a1; bili_jct=8a2be0cec3ea44021fe2e1b2e9c505a6; _uuid=3E976774-5297-B938-35D4-B99BF753B4BF74970infoc; fingerprint3=877125c9294b468f9a335a5cd082ae15; fingerprint=c5ae947e8dd6ce473417eaf81dcf1cb4; buivd_fp=B0D9BECB-D695-414B-846A-B2EDA4C7857640772infoc; buvid_fp_plain=B0D9BECB-D695-414B-846A-B2EDA4C7857640772infoc; fingerprint_s=7781f651d0a5912032bec8892fc2728d; LIVE_PLAYER_TYPE=1; rpdid=|(u))uuYkk)u0J'uY|mRm|lYR; CURRENT_QUALITY=64; bp_t_offset_447571231=478316965730327065; PVID=4; bp_video_offset_447571231=480769847321573018; bfe_id=fdfaf33a01b88dd4692ca80f00c2de7f",

'sec-ch-ua-mobile': '?0',
'Sec-Fetch-Dest': 'document',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-Site': 'none',
'Sec-Fetch-User': '?1',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
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