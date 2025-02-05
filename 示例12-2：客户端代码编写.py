# 示例12-2：客户端代码编写
import socket # 客户端相较于服务器，这里直接导入即可

# 1 使用socket类创建一个套接字对象
client_socket = socket.socket() # 客户端这里与服务器一致，但不需要加参数


# 2 使用connect设置连接的主机IP和主机设置的端口号
ip='666.666.6.666' # 本机ip地址，等同于local

port=8888 # 端口0~65535

client_socket.connect((ip,port))# 括号里是个元组

print("服务器建立连接成功")


# 3 使用recv() / send()方法接收/发送数据
    # 服务器是recv()则客户端就是send()
client_socket.send("welcome".encode('utf-8')) # 服务器和客户端的编码格式必须一致


# 4 使用close()关闭套接字
client_socket.close()
print("发送完毕")

# 注意要先启动服务器端，等待客户端发送信息
















