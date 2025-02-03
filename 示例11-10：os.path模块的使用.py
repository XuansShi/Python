# 示例11-10：os.path模块的使用
import os.path
# 1 获取目录或文件的绝对路径
print(os.path.abspath('test.txt'))

# 2 判断目录或文件在磁盘上是否存在
print(os.path.exists('test.txt'))


# 3 拼接路径
print(os.path.join('D:\\xxzl\\biancheng\\Python\\Python_CODE\\pythonProject1\\chapt11','test.txt'))



# 4 分别获取文件名和后缀名
print(os.path.splitext('test.txt'))



# 5 从路径中提取文件名
print(os.path.basename('D:\\xxzl\\biancheng\\Python\\Python_CODE\\pythonProject1\\chapt11\\test.txt'))


# 6 提取路径（不包含文件名）
print(os.path.dirname('D:\\xxzl\\biancheng\\Python\\Python_CODE\\pythonProject1\\chapt11\\test.txt'))


# 7 判断是否为有效路径
print(os.path.isdir('D:\\xxzl\\biancheng\\Python\\Python_CODE\\pythonProject1\\chapt11'))


# 8 判断是否为有效文件
print(os.path.isfile('D:\\xxzl\\biancheng\\Python\\Python_CODE\\pythonProject1\\chapt11\\test.txt'))












