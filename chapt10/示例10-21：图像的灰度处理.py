# 示例10-21：图像的灰度处理
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')  # 切换到 TkAgg 后端;chatgpt:你的问题是由于使用了 PyCharm 的 Matplotlib 后端与图形显示功能存在兼容性问题，AttributeError: 'FigureCanvasInterAgg' object has no attribute 'tostring_rgb' 表明当前 Matplotlib 的后端不支持 plt.show() 的图像渲染。可以通过以下几种方法解决：

# 读取图片
n1 = plt.imread('x1s0.jpg')
print(type(n1),n1) # 打印n1得到三维数组，最高维度是图像的高，次高维度是图像的宽，最低维度是[R,G,B]

plt.imshow(n1)

# 编写一个灰度的公式
    # 创建数组
n2 = np.array([0.299,0.587,0.114])

# 将数组n1 (RGB颜色值) 与数组n2(灰度公式固定值)进行点乘运算
x=np.dot(n1,n2)
plt.imshow(x,cmap="gray")

#显示图像
plt.show()










