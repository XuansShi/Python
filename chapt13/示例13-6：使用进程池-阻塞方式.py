# 示例13-6：使用进程池-阻塞方式
from multiprocessing import Pool
import time,os

# 编写任务
def task(name):
    print(f'子进程PID：{os.getpid()}，父进程PID：{os.getppid()}')
    time.sleep(2)

if __name__ == '__main__':
    # 主进程
    start = time.time()
    print ("父进程开始执行")
    # 创建进程池
    p = Pool(3)

    # 创建任务
    for i in range(10):
        # 以阻塞的方式
        p.apply(func=task, args=(i,))

    # 无需手动start，记得关闭就行

    p.close()# 关闭进程池，不再接收新任务
    p.join()# 阻塞父进程，等待所有子进程执行完毕
    print("所有子进程执行完毕，父进程执行结束")
    print("执行用时：",time.time() - start)






















