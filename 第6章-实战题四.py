# 第6章-实战题四
# 包含模块re
import re

# 待查找字符串
s='"queryEnc":"%C3%C0%C5%AE","queryExt":"美女","listNum":1726,"displayNum":1102160,"gsm":"3c","bdFmtDispNum":"约1,100,000","bdSearchTime":"","isNeedAsyncRequest":0,"bdIsClustered":"1","data":[{ "adType":"0", "hasAspData":"0","thumbURL":"https://img1.baidu.com/it/u=272155668,1962283813&fm=26&fmt=auto","commodityInfo":null, "isCommodity":0, "middleURL":"https://img1.baidu.com/it/u=272155668,1962283813&fm=26&fmt=auto", "shituToken":"aadb3a", "largeTnImageUrl":"", "hasLarge" :0, "hoverURL":"https://img1.baidu.com/it/u=272155668,1962283813&fm=26&fmt=auto", "pageNum":30, "objURL":"ipprf_z2C$qAzdH3FAzdH3F2t42d_z&e3Bkwt17_z&e3Bv54AzdH3Ft4w2j_fjw6viAzdH3Ff6v=ippr%nA%dF%dFetn_z&e3Bxt78dn_z&e3Bvg%dFstej%dFda8l%dFam%dFdl%dF88%dF8ande8cm80ban0nllalnba80_z&e3B3r2&6juj6=ippr%nA%dF%dFetn_z&e3Bxt78dn_z&e3Bvg&wrr=daad&ftzj=ullll,8aaaa&q=wba&g=a&2=ag&u4p=3rj2?fjv=8m9abc98cd&p=an8vwcw9v9jl1nm88jdllww8dmuwnvvn", "fromURL":"ippr_z2C$qAzdH3FAzdH3Fe_z&e3Bm_z&e3BvgAzdH3Fr65utsjAzdH3FowpviMtgt_z&e3Brir?et1=m8adm8", "fromJumpUrl":"ippr_z2C$qAzdH3FAzdH3Fe_z&e3Bm_z&e3BvgAzdH3Fr65utsjAzdH3FowpviMtgt_z&e3Brir?et1=m8adm8", "fromURLHost":"v.6.cn", "currentIndex":"", "width":800, "height":600, "type":"jpg", "is_gif":0, "isCopyright":0, "resourceInfo":null, "strategyAssessment": "3141544242_1243_0_0", "filesize":"", "bdSrcType":"0", "di":"157630", "pi": "0", "is":"0,0", "imgCollectionWord":"","hasThumbData":"0", "bdSetImgNum":0, "partnerId":0, "spn":0, "bdImgnewsDate":"2020-06-03 02:31","fromPageTitle":"美女<\/strong>热舞", "fromPageTitleEnc":"美女热舞","bdSourceName":"", "bdFromPageTitlePrefix":"", "isAspDianjing":0, "token":"", "imgType" : "", "cs" : "272155668,1962283813", "os" : "1570395708,812629700", "simid" : "272155668,1962283813", "personalized":"0","simid_info":null,"face_info":null,"xiangshi_info":null,"adPicId":"0","source_type":""},{ "adType":"0", "hasAspData":"0","thumbURL":"https://img0.baidu.com/it/u=1934854801,2871685401&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=313","commodityInfo":null, "isCommodity":0, "middleURL":"https://img0.baidu.com/it/u=1934854801,2871685401&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=313", "shituToken":"9bb791", "largeTnImageUrl":"", "hasLarge" :0, "hoverURL":"https://img0.baidu.com/it/u=1934854801,2871685401&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=313", "pageNum":31, "objURL":"ipprf_z2C$qAzdH3FAzdH3F2t42d_z&e3Bkwt17_z&e3Bv54AzdH3Ft4w2j_fjw6viAzdH3Ff6v=ippr%nA%dF%dFt42_z&e3B33da_z&e3Bv54%dF7r%dFwsst42%dF8889%dFac8dd8aSlnl%dFd8ac8daSlnl-d-8daa_z&e3B3r2&6juj6=ippr%nA%dF%dFt42_z&e3B33da_z&e3Bv54&wrr=daad&ftzj=ullll,8aaaa&q=wba&g=a&2=ag&u4p=3rj2?fjv=8m9abc98cd&p=bmcukd9vmml18lau1mjdub9dnnlmnakd"'

# 模式字符串
pattern='https://img\d{1}.baidu.com/it/u=\d*,\d*&fm=\d*&fmt=auto' # 模式字符串

lst=re.findall(pattern,s)

for item in lst:
    print(item)


