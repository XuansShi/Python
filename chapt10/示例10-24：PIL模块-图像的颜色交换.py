# 示例10-24：PIL模块-图像的颜色交换
from PIL import Image

# 加载图片
im = Image.open('x1s0.jpg')

# 查看图像信息
print(im,type(im))

# 提取RGB图像的颜色通道，返回结果是图像的脚本
    # 系列解包赋值
r,g,b = im.split()
    # 合并通道
om = Image.merge('RGB',(r,b,g)) # 这里改RGB交换的顺序
    # 保存
om.save('new_x1s0.jpg')





