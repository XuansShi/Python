# 示例12-1：服务器端代码编写
from socket import socket, AF_INET, SOCK_STREAM # 导入类
    # AF_INET用于Internet之间的进程通信
    # SOCK_STREAM表示TCP协议

# 1 创建socket对象
server_socket = socket(AF_INET, SOCK_STREAM)# 这两个参数都大写了，代表常量


# 2 使用bind方法 绑定IP地址和端口号
ip='666.666.6.666' # 本机ip地址，等同于local

port=8888 # 端口0~65535

server_socket.bind((ip,port)) # 括号里是个元组

# 3 使用listen方法 开始TCP监听
server_socket.listen(5)
print('waiting for a connection')

# 4 使用accept方法 等待客户端的连接
client_socket,client_addr = server_socket.accept()# 返回客户端的一个socket对象和一个client地址
    # 没有客户端会一直卡在第4步

# 5 使用recv() / send()方法接收/发送数据
data = client_socket.recv(1024)
print("客户端发送来的数据",data.decode("utf-8")) # 以utf-8规则解码（注意发送和接收时的规则必须一直）

# 6 使用close()关闭套接字
server_socket.close()




