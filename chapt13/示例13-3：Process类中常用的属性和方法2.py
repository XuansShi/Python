# 示例13-3：Process类中常用的属性和方法2
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
    # 主进程
    print("主进程开始执行")
    for i in range(5):
        # 创建第一个子进程
        p1= Process(target=sub_process1(),args= ("xs",)) # 如果Process创建对象时没有指定target的参数，那么就会调用Process类的run方法，而不是自己写的方法

        # 创建第二个子进程
        p2= Process(target=sub_process2(),args= (18,))

        p1.start() # Process创建对象时指定了target的参数，此时调用指定的方法执行
        p2.start()

        # 终止进程
        p1.terminate()
        p2.terminate()
    print("主进程执行结束")







