# 示例13-8：队列的基本使用
from multiprocessing import Queue
if __name__ == '__main__':
    q = Queue(3)# 创建一个最多可接受3条信息的队列
    # 1 队列是否为空
    print(q.empty())

    # 2 队列是否为满
    print(q.full())

    # 3 put想队列添加信息
    q.put("hello")
    q.put("world")

    print("队列是否为空",q.empty())
    print("队列是否为满",q.full())

    q.put(1)
    print("队列是否为空",q.empty())
    print("队列是否为满",q.full())


    # 4 队列中包含的信息个数
    print("队列中包含的信息个数",q.qsize())

    # 5 get出队
    print(q.get())
    print("队列中包含的信息个数", q.qsize())

    # 6 put_nowait 入队 不等待
    q.put_nowait(2)
    # q.put_nowait(3)# 报错，队列已满

    # 7 put 入队 等待直到有空位置时再入队
    # q.put(3)


    # 遍历
    if not q.empty():
        for i in range(q.qsize()):
            print(q.get_nowait())

    print("队列是否为空",q.empty())
    print("队列是否为满",q.full())
