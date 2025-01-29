# 示例10-22：Pandas与matplotlib绘制饼图
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')  # 切换到 TkAgg 后端;chatgpt:你的问题是由于使用了 PyCharm 的 Matplotlib 后端与图形显示功能存在兼容性问题，AttributeError: 'FigureCanvasInterAgg' object has no attribute 'tostring_rgb' 表明当前 Matplotlib 的后端不支持 plt.show() 的图像渲染。可以通过以下几种方法解决：

# 读取Excel文件
df = pd.read_excel("景区天气.xlsx")
print(df)


# 解决绘图中文乱码问题
plt.rcParams['font.sans-serif'] = ['SimHei']  #改成一个你计算机上有的字体”SimHei“

# 设置画布的大小
plt.figure(figsize=(10, 6))

# 制作饼图各部分的标签
v = df["景区"]

# 定义一个表示数字数据的变量
t = df["时间"]

print(v)
print(t)

# 绘制饼图
plt.pie(t, labels=v, autopct='%1.1f%%',startangle=90) # 数据 , 标签 , 固定的小数格式 , 角度(非必须，设为90度一般会好看一点)

# 设置x,y刻度 ，保证正圆
plt.axis('equal')

# 设置饼图的标题
plt.title("示例10-22：Pandas与matplotlib绘制饼图")

# 显示
plt.show()