# 示例10-16：爬取二进制数据-图片
import requests
url='https://act-webstatic.mihoyo.com/puzzle/bh3/pz_WKLA2Jeh9z/resource/puzzle/2025/01/20/535582655a92f8601e3af78df57c2cbb_9181798926822935183.png?x-oss-process=image/format,webp/quality,Q_90'
req=requests.get(url)

# 保存到本地
with open('x1s0.png','wb') as file:
    file.write(req.content) # 图片的二进制数据在返回对象req的content里










