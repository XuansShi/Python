
import requests
url ="https://cn-hbwh-fx-01-01.bilivideo.com/upgcxcode/66/21/27629062166/27629062166-1-100024.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1735654032&gen=playurlv2&os=bcache&oi=3746356498&trid=0000067afb3a6a304503b554152a29e166d7u&mid=475710230&platform=pc&og=hw&upsig=94132de7e3fc68073c324a51e15a43f9&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform,og&cdnid=3871&bvc=vod&nettype=0&orderid=0,3&buvid=7ABA68ED-C34E-365A-3EAD-2287F39B7A3E64743infoc&build=0&f=u_0_0&agrr=0&bw=126938&np=151388311&logo=80000000"

wz={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',"refer":"https://www.bilibili.com/video/BV1E86HYPEZf/?spm_id_from=333.788.top_right_bar_window_dynamic.content.click&vd_source=e16890b3bc400ded1fbeb665df23a933"}


res = requests.get(url,headers=wz)

open("爬取的视频.mp4","wb").write(res.content)

print(res.status_code)


