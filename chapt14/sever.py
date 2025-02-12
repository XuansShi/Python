# coding:utf-8#
# sever
import threading
import time
from socket import socket, AF_INET, SOCK_STREAM
import wx
class XsServer(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,id=1002,title="TAG工作室",pos=wx.DefaultPosition,size=(400,450))
        # 窗口放一个面板
        pl = wx.Panel(self)
        # 面板上放盒子
        box= wx.BoxSizer(wx.VERTICAL)# 垂直方向自动排版布局

        # 可伸缩的网格布局
        fgzl= wx.FlexGridSizer(wx.HSCROLL) # 水平方向布局

        start_server_btn =  wx.Button(pl,size=(133,40),label="启动服务")
        stop_server_btn =  wx.Button(pl,size=(133,40),label="停止服务")
        record_btn =  wx.Button(pl,size=(133,40),label="保存聊天记录")

        # 放到可伸缩的网格布局中
        fgzl.Add(start_server_btn,1,wx.TOP)
        fgzl.Add(stop_server_btn,1,wx.TOP)
        fgzl.Add(record_btn,1,wx.TOP)

        # 将可伸缩的网格布局放入box
        box.Add(fgzl,1,wx.ALIGN_CENTER)


        # 只读的多行文本框，显示聊天内容
        self.show_text = wx.TextCtrl(pl, size=(400, 410),   style=wx.TE_MULTILINE | wx.TE_READONLY)  # 参数：放入所属的面板名称 大小 方式（多行 逻辑或| 只读）
        # 把文本框添加到box中
        box.Add(self.show_text, 1, wx.ALIGN_CENTER)

        # 把盒子放入面板
        pl.SetSizer(box)
        #——————————————————————————————————↑界面绘制↑——————————————————————————————————————

        #——————————————————————————————————↓服务器功能实现必要属性↓——————————————————————————————————————
        self.isOn = False #存储服务器启动状态
        # 服务器绑定的IP和端口
        self.host_port= ('', 8888)

        # 创建socket对象
        self.server_socket = self(AF_INET, SOCK_STREAM)

        # 绑定IP地址和端口号
        self.server_socket.bind(self.host_port)

        # 监听
        self.server_socket.listen(5)

        # 创建一个字典，存储与客户端对话的会话线程
        self.session_thread_dict = {} # key:客户端的名称 value:会话线程

        # 鼠标点击按钮时执行的操作
        self.Bind(wx.EVT_BUTTON,self.start_server,start_server_btn) #参数： wx.EVT_BUTTON(绑定事件) 绑定一个方法 绑定一个按钮

        # 给保存聊天记录按钮绑定事件
        self.Bind(wx.EVT_BUTTON, self.save_record, record_btn)

        # 给断开按钮绑定事件
        self.Bind(wx.EVT_BUTTON, self.stop_sever, stop_server_btn)


    def stop_server(self, event):
        print("服务器已停止服务")
        self.isOn = False


    def start_server(self,event):
        # 获取只读文本框中的内容
        record_data = self.show_text.GetValue()
        with open("record.log","w",encoding = 'utf-8') as file:
            file.write(record_data)




    def start_server(self,event):
        #print("启动服务的按钮被点击了")
        # 判断服务器是否已经启动
        if self.isOn: # 等价于self.isOn == False
            # 没有启动时启动服务器
            self.isOn = True
            # 创建主线程对象，函数式创建主线程
            main_thread = threading.Thread(target=self.do_work)
            # 设置为守护线程，父线程执行结束（窗体界面）子线程也自动关闭
            main_thread.daemon = True
            # 启动主线程
            main_thread.start()

    def do_work(self):
        # 判断服务器是否已经启动
        while self.isOn:
            # 接收客户端的连接请求
            session_socket,client_addr = self.server_socket.accept()
            # 客户端发送连接请求后，发送来的第一条数据为客户端名称，客户端的名称作为字典中的键
            user_name= session_socket.recv(1024).decode('utf-8')

            # 创建一个会话线程对象
            sesstion_thread = threading.Thread(session_socket,user_name,self)

            # 存储到字典中
            self.session_thread_dict[user_name]=sesstion_thread

            # 启动会话线程
            sesstion_thread.start()

            # 输出服务器的提示信息
            self.show_info_and_send_client(f"服务器通知，欢迎f{user_name}进入聊天室",time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))

        # self.isOn的值为False时，关闭socket对象
        self.server_socket.close()

    def show_info_and_send_client(self,data_source,data,data_time):
        # 字符串拼接操作
        send_data = f"{data_source}:{data}\n{data_time}"

        # 显示到只读文本框
        self.show_text.AppendText("-"*40+"\n"+send_data+'\n')

        # 遍历字典，每一个客户端都发送一次
        for client in self.session_thread_dict.values():
            # 判断当前会话是否是开启状态
            if client.isOn:
                client.client_socket.send(send_data.encode('utf-8'))




# 服务器端会话线程的类
class SesstionThread(threading.Thread):
    def __init__(self,client_socket,user_name,server):
        # 调用父类的初始化方法
        threading.Thread.__init__(self)
        self.client_socket = client_socket
        self.user_name = user_name
        self.server = server
        self.isOn= True # 会话线程是否启动，创建SessionThread对象时启动

    def run(self)->None:
        print(f"客户端{self.user_name}已经和服务器连接成功，服务器启动一个会话线程")
        while self.isOn:
            # 从客户端接收线程，存储到data中
            data = self.client_socket.recv(1024).decode('utf-8')
            # 如果客户端点击断开按钮，先给服务器发送一句话
            if data == "bye":
                self.isOn = False
                # 发送一条通知
                self.server.show_info_and_send_client("服务器通知：",f"{self.user_name}离开了聊天室",time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))

            else:
                # 如果是其他聊天信息就显示给所有客户端以及服务器
                self.server.show_info_and_send_client(self.user_name,data,time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))

        # 关闭socket
        self.client_socket.close()


if __name__ == '__main__':
    # 初始化
    app = wx.App()

    # 创建自己的客户端界面对象
    server = XsServer()
    server.Show()

    # 循环刷新显示
    app.MainLoop()




