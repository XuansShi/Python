# 示例13-11：使用队列实现进程间的通信
from multiprocessing import Process,Queue
import time
a = 100
def write_msq(q):# 传入要操作的变量
    global a # 声明全局变量a
    if not q.full():
        for i in range(6):
            a -= 10
            q.put(a)
            print("a入队时的值",a)



# 出队
def read_msq(q):
    time.sleep(1)
    while not q.empty():
        print("出队时a的值：",q.get())

if __name__ == '__main__':
    print("父进程开始执行")

    q = Queue() # 由父进程创建队列，没有指定参数，说明可接收的消息没有上限
        # 这个队列是两个子进程共享的，可以用来实现进程间的通信

    # 创建两个子进程
    p1 = Process(target=write_msq, args=(q,))
    p2 = Process(target=read_msq, args=(q,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("父进程完毕")