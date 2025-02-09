# 示例13-12：函数方式创建线程
import threading
from threading import Thread
import time

# 编写函数
def test():
    for i in range(3):
        time.sleep(1)
        print(f"线程{threading.current_thread().name}正在执行{i}")

if __name__ == '__main__':
    start = time.time()
    print("主线程开始执行")

    # 创建2个子线程
    lst = [Thread(target=test) for i in range(2)] # 生成两个线程对象
    for i in lst:
        #启动线程
        i.start()

    for item in lst:
        item.join()# 阻塞主线程

    print(f"一共耗时{time.time()-start}")


'''
这里面有一个进程，其中包括三个线程
主线程负责执行main中的代码
Thread-1线程执行三次循环
Thread-2线程执行三次循环
三个线程并发执行，谁先执行不一定

'''





