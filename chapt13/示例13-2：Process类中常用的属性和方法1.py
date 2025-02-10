# 示例13-2：Process类中常用的属性和方法1
from multiprocessing import Process
import time,os

# 函数式方式创建子进程
def sub_process1(name):
    print(f'子进程PID：{os.getpid()}，父进程PID：{os.getppid()},---------{name}')

    time.sleep(1)

def sub_process2(name):
    print(f'子进程PID：{os.getpid()}，父进程PID：{os.getppid()},---------{name}')

    time.sleep(1)

if __name__ == '__main__':
    for i in range(5):
        # 创建第一个子进程
        p1 = Process(target=sub_process1(),args=('xs',)) #位置参数args需要用元组传参
        # 创建第二个子进程
        p2 = Process(target=sub_process2(),args=('6',))

        # 启动子进程
        p1.start()
        p2.start()

        print(p1.name,"是否执行完毕：",p1.is_alive())
        print(p2.name, "是否执行完毕",p2.is_alive())

        print(p1.name,"pid是",p1.pid)
        print(p2.name,"pid是",p2.pid)

        p1.join() #主进程要等p1执行结束，阻塞主进程
        p2.join()

        print(p1.name,"是否执行完毕：",p1.is_alive())
        print(p2.name, "是否执行完毕",p2.is_alive())

    print("父进程执行完毕")




