# 第10章-实战题三：词云图
from wordcloud import WordCloud # 从wordcloud模块导入WordCloud类
import jieba

# 读取数据
with open('jieba.txt','r',encoding="utf-8") as file:
    s=file.read()

# 中文分词
lst= jieba.lcut(s)

# 排除词
stopword=["速度","效果","性能"]

# 利用空格拼接列表内元素
txt=''.join(lst)

# 绘制词云图
wordcloud=WordCloud(background_color='white',front_path="msyh.ttc",stopwords=stopword,width=800,height=600)

'''
在这段代码中，WordCloud 类的各个参数配置如下：

1. background_color
作用：设置词云背景颜色。
值：可以是字符串类型的颜色名（如 'white'），或是十六进制颜色代码（如 '#ffffff'）。
示例：background_color='white' 设置背景颜色为白色。

2. font_path
作用：设置字体路径，用于显示中文。
值：文件路径，指向一个支持中文的字体文件。如果不设置，词云图将无法正确显示中文，特别是在处理中文文本时。
说明：front_path="msyh.ttc" 中的 "msyh.ttc" 是字体文件路径（微软雅黑字体），你需要确保在你的计算机中有这个字体文件，或者提供一个正确的字体路径。
示例：font_path='msyh.ttc'，确保 'msyh.ttc' 是你机器上的一个有效字体文件，通常是“微软雅黑”字体的文件。

3. stopwords
作用：设置需要排除的词汇。词云生成时会忽略这些词。
值：可以是一个词汇集合，包含你希望排除的词语。
示例：stopwords=stopword，在这里，stopword 是你定义的一个列表，包含了不需要显示的词，如 "速度", "效果", "性能"。

4. width 和 height
作用：设置词云图的宽度和高度，单位为像素。
值：正整数。
示例：width=800, height=600 设置词云图的宽度为 800 像素，高度为 600 像素。

5. generate()
作用：生成词云图。需要传入文本数据（如你通过分词得到的文本）。
示例：wordcloud.generate(txt)，txt 是通过分词得到的文本，它包含了需要生成词云图的所有词。

6. to_file()
作用：将生成的词云图保存为图片文件。
示例：wordcloud.to_file('wordcloud.png')，将词云图保存为 wordcloud.png 文件。
'''


# 点出调用generate，生成词云图
wordcloud.generate(txt)

# 保存图片
wordcloud.to_file('wordcloud.png')