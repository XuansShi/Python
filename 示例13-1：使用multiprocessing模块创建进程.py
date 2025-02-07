# 示例13-1：使用multiprocessing模块创建进程
from multiprocessing import Process
import os,time
# 使用函数方式创建进程，函数中的代码是进程要执行的代码
def test():
    print(f"我是子进程，我的PIP是：{os.getpid()},我的父进程是:{os.getppid()}")
    time.sleep(1)

if __name__ == '__main__':
    print("主进程开始执行")
    lst=[]
    # 创建5个子进程
    for i in range(5):
        # 创建子进程
        p = Process(target=test)# 五个参数，其中target必须要写
        # 启动子进程
        p.start()
        # 启动中的进程添加到列表中
        lst.append(p)

    # 遍历lst列表中的5个子进程
    for item in lst:
        item.join()# 阻塞主进程，执行完子进程后再执行主进程

    print("主进程执行结束")

















