# 示例13-16：使用lock锁
import threading
from threading import Thread,Lock
import time

# 创建锁对象
lock_obj = Lock()

ticket = 50

def sale_ticket():
    global ticket
    for i in range(100):
        lock_obj.acquire()  # 给每个判断的过程上锁即可
        if ticket > 0:
            print(f"{threading.current_thread().name}正在出售第{ticket}张票")
            ticket -= 1
        time.sleep(1)

        lock_obj.release() # 释放锁


if __name__ == '__main__':
    for i in range(3):
        t = Thread(target=sale_ticket)
        t.start()






