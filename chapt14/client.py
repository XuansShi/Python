# coding:utf-8
# client
import threading
import time
import wx
from socket import socket, AF_INET, SOCK_STREAM

class XsClient(wx.Frame):
    def __init__(self,client_name):
        # 调用父类的初始化方法

        wx.Frame.__init__(self,None,id = 1001,title=client_name+"的客户端界面",pos=wx.DefaultPosition,size=(400,450))
        '''
        None 没有父级窗口
        id 当前窗口编号
        pos=wx.DefaultPosition 窗体打开位置 设置为 默认
        size 窗体大小，单位像素 此处为400宽 450高
        '''

        # 创建面板对象
        pl= wx.Panel(self)

        # 在面板中放上盒子
        box = wx.BoxSizer(wx.VERTICAL) # wx.VERTICAL垂直方向自动排版布局


        # 可伸缩的网格布局1
        fgzl = wx.FlexGridSizer(wx.HORIZONTAL) # wx.HORIZONTAL水平方向布局

        # 创建两个按钮 连接 断开
        conn_btn = wx.Button(pl,size=(200,40),label = "连接")
        dis_conn_btn = wx.Button(pl,size=(200,40),label = "断开") # 参数： 放入所属的面板名 大小 文字
        # 把两个按钮放到可伸缩网格布局1中
        fgzl.Add(conn_btn,1,wx.TOP|wx.LEFT) # 参数： 放入的按钮名称 随便赋予一个整数值 按钮位置（上方左边）
        fgzl.Add(dis_conn_btn,1,wx.TOP|wx.RIGHT) # 参数： 放入的按钮名称 随便赋予一个整数值 按钮位置（上方右边）



        # 把网格布局1添加到box中
        box.Add(fgzl,1,wx.ALIGN_CENTER) # 参数： 放入的网格布局名称 随便赋予一个整数值 位置（居中对齐）

        # 只读的多行文本框，显示聊天内容
        self.show_text = wx.TextCtrl(pl,size=(400,210),style=wx.TE_MULTILINE | wx.TE_READONLY)# 参数：放入所属的面板名称 大小 方式（多行 逻辑或| 只读）
         # 把文本框添加到box中
        box.Add(self.show_text,1,wx.ALIGN_CENTER)



        # 创建聊天内容的文本框
        self.chat_text= wx.TextCtrl(pl,size=(400,120),style=wx.TE_MULTILINE | wx.TE_READONLY)
            # 把文本框添加到box中
        box.Add(self.chat_text,1,wx.ALIGN_CENTER)





        # 可伸缩的网格布局2
        fgzl2 = wx.FlexGridSizer(wx.HORIZONTAL) # wx.HORIZONTAL水平方向布局

        # 创建两个按钮  重置 发送
        reset_btn = wx.Button(pl, size=(200, 40), label="重置")
        send_btn = wx.Button(pl, size=(200, 40), label="发送")  # 参数： 放入所属的面板名 大小 文字
        # 把两个按钮放到可伸缩网格布局2中
        fgzl2.Add(reset_btn, 1, wx.TOP | wx.LEFT)  # 参数： 放入的按钮名称 随便赋予一个整数值 按钮位置（上方左边）
        fgzl2.Add(send_btn, 1, wx.TOP | wx.RIGHT)  # 参数： 放入的按钮名称 随便赋予一个整数值 按钮位置（上方右边）

        # 把网格布局2添加到box中
        box.Add(fgzl2,1,wx.ALIGN_CENTER) # 参数： 放入的网格布局名称 随便赋予一个整数值 位置（居中对齐）



        # 将盒子放到面板中
        pl.SetSizer(box)

        #——————————————————————————————————↑客户端界面绘制↑——————————————————————————————————————

        # 绑定按钮
        self.Bind(wx.EVT_BUTTON,self.connect_to_server,conn_btn)

        # 实例属性的设置
        self.client_name=client_name
        self.isConnected=False # 存储客户端连接服务器的状态
        self.client_socket=None # 设置客户端的socket对象为空

        # 给发送按钮绑定事件
        self.Bind(wx.EVT_BUTTON,self.connect_to_server,send_btn)

        # 给断开按钮绑定事件
        self.Bind(wx.EVT_BUTTON,self.dis_conn_server,dis_conn_btn)

        # 给重置按钮绑定事件
        self.Bind(wx.EVT_BUTTON,self.reset,reset_btn)


    def reset(self,event):
        self.chat_text.Clear() # 文本框内容清空



    def dis_conn_server(self,event):
        # 发送断开信息
        self.client_socket.send("disconnect".encode('utf-8'))

        # 改变连接状态
        self.isConnected=False


    def connect_to_server(self,event):
        # 判断连接状态
        if self.isConnected:
            # 从可写文本框中获取数据
            input_data = self.chat_text.GetValue()
            if input_data != "":
                # input_data 不为空，向服务器端发送数据
                self.client_socket.send(input_data.encode('utf-8'))

                # 发完数据后，清空文本框
                self.chat_text.SetValue('')

    def connect_to_server(self,event):
        print(f"客户端{self.client_name}连接服务器成功")
        # 如果没有连接服务器则开始连接
        if not self.isConnected: # 等价于self.isConnected == False
            # TCP编程
            server_host_port = ('127.0.0.1',8888)
            #self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   由于导入的时候是直接由模块导入类，所以使用的时候不需要再用模块的名称了，改成下一行那样
            self.client_socket = socket(socket.AF_INET, socket.SOCK_STREAM)


            # 发送连接请求
            self.client_socket.connect(server_host_port)

            # 连接成功后立刻发送一条数据
            self.client_socket.send(self.client_name.encode("utf-8"))

            # 启动一个线程，客户端的线程与服务器端的会话线程进行会话
            client_thread = threading.Thread(target = self.recv_data())

            #设置为守护线程 (窗体关掉，子线程也结束了)
            client_thread.daemon = True

            # 修改连接状态
            self.isConnected=True

            # 启动线程
            client_thread.start()

    def recv_data(self):
        # 判断是否为连接状态
        while self.isConnected:
            # 接收来自服务器的数据
            data = self.client_socket.recv(1024)

            # 显示到只读文本框
            self.show_text.AppendText("-"*40+"\n"+data+"\n")


if __name__ == '__main__':
    # 初始化
    app = wx.App()


    # 创建自己的客户端界面对象
    name = input("请输入客户端名称")
    client = XsClient(name)
    client.Show()

    # 循环刷新显示
    app.MainLoop()





