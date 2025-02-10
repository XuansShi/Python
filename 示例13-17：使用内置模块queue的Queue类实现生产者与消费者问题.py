# 示例13-17：使用内置模块queue的Queue类实现生产者与消费者问题
from queue import Queue
from threading import Thread
import time

# 创建一个生产者类
class Producer(Thread):
    def __init__(self,name, queue):
        Thread.__init__(self,name= name)
        self.queue = queue
    def run(self):
        for i in range(1,6):
            print(f"{self.name}将产品{i}放入队列")
            self.queue.put(i)
            time.sleep(1)
        print("生产者完成了所有数据的存放")

# 创建一个消费者类
class Consumer(Thread):
    def __init__(self,name,queue):
        Thread.__init__(self,name= name)
        self.queue = queue
    def run(self):
        for _ in range(1,6):
            value = self.queue.get()
            print(f"消费者线程：{self.name}取出了{value}")
            time.sleep(1)
        print("消费者线程完成了所有数据的取出")

# 主线程
if __name__ == '__main__':
    # 创建队列
    queue = Queue()

    # 创建生产者线程
    p=Producer("Producer", queue)

    # 创建消费者线程
    c = Consumer("Consumer", queue)

    c.start()
    p.start()
    c.join()
    c.join()
    print("主线程执行结束")








