# 示例12-3：TCP多次通信服务器端代码编写
import socket

# 1 创建socket对象
socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2 绑定主机和IP端口
socket_obj.bind(('666.666.6.666',8888))

# 3 设置最大的连接数量
socket_obj.listen(5)

# 4 等待客户端的TCP连接
client_socket,client_addr = socket_obj.accept()


# 5 接收数据，并且解码
info = client_socket.recv(1024).decode('utf-8')      # 5.1 初始化变量

while info !='bye':                               # 5.2 条件判断
    if info !='':
        print("接收到的数据是：",info)               # 5.3 循环体

    # 准备发送的数据
    data=input("请输入要发送的数据：")

    # 服务器回复客户端
    client_socket.send(data.encode('utf-8'))# send的时候要记得编码
    if data =="bye":
        break
    info = client_socket.recv(1024).decode('utf-8')   # 5.4 改变变量

# 6 关闭socket对象
client_socket.close()
socket_obj.close()





