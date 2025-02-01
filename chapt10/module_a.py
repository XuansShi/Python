# 示例10-8：
'''
    # 如果不在module_a中使用主程序，那么导入模块后会自动运行其中的代码
print("welcome to Beijing")
name = ("python")
print(name)
'''


if __name__ == '__main__':
    print("welcome to Beijing")
    name = ("python")
    print(name)

# 主程序阻止了全局变量的数据被输出运行
