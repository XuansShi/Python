# 示例13-10：设置put方法的参数
from multiprocessing import Queue
if __name__ == '__main__':
    q = Queue(3)
    # 向队列添加元素
    q.put(1)
    q.put(2)
    q.put(3)

    q.put(4,block=True,timeout=2)  # timeout=2 插入前等待2秒，此后如果还没有空位置就抛出异常










