# 示例13-9：向已满的队列中添加新元素
from multiprocessing import Queue
if __name__ == '__main__':
    q = Queue(3)
    # 向队列添加元素
    q.put(1)
    q.put(2)
    q.put(3)
    # 此时已满不能插入











