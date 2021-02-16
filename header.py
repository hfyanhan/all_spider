from pub_net import ua


user_agent=ua()

header1={
'Host': "api.bilibili.com",
'sec-ch-ua':'''"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"''',
'sec-ch-ua-mobile': '?0',
'Sec-Fetch-Dest': 'document',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-Site': 'none',
'Sec-Fetch-User': '?1',
#'Cookie':"buvid3=B0D9BECB-D695-414B-846A-B2EDA4C7857640772infoc; LIVE_BUVID=AUTO8515593048657300; pgv_pvi=152973312; sid=b53gif2j; blackside_state=1; CURRENT_FNVAL=80; DedeUserID=447571231; DedeUserID__ckMd5=6bf16ff15c0a360b; SESSDATA=724a5e12%2C1617290904%2Cd85c1*a1; bili_jct=8a2be0cec3ea44021fe2e1b2e9c505a6; _uuid=3E976774-5297-B938-35D4-B99BF753B4BF74970infoc; fingerprint3=877125c9294b468f9a335a5cd082ae15; fingerprint=c5ae947e8dd6ce473417eaf81dcf1cb4; buivd_fp=B0D9BECB-D695-414B-846A-B2EDA4C7857640772infoc; buvid_fp_plain=B0D9BECB-D695-414B-846A-B2EDA4C7857640772infoc; fingerprint_s=7781f651d0a5912032bec8892fc2728d; LIVE_PLAYER_TYPE=1; rpdid=|(u))uuYkk)u0J'uY|mRm|lYR; CURRENT_QUALITY=32; PVID=1; bfe_id=fdfaf33a01b88dd4692ca80f00c2de7f; bp_video_offset_447571231=489647007855878298; bp_t_offset_447571231=489648390831177606",
'Upgrade-Insecure-Requests': '1',
'User-Agent': user_agent
}
header2={"User-Agent": user_agent,
	      "Referer": "https://www.bilibili.com/ranking/all/0/0/3"
        }
