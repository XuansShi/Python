# 示例13-13：使用Thread子类创建线程
import threading
from threading import Thread
import time

class SubThread(Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            print(f"线程：{threading.current_thread().name}正在执行{i}")

if __name__ == '__main__':
    print("主线程开始执行")
    lst = [SubThread() for i in range(2)]
    for i in lst:
        i.start()

    for i in lst:
        i.join()
    print("主线程执行完毕")










