# 示例12-4：TCP多次通信客户端代码编写
import socket

# 1 创建socket对象
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2 绑定主机ip和端口
client_socket.connect(('666.666.6.666', 8888))
print("已建立服务器连接")


# 3 客户端发送数据
info = ''
while info !='bye':
    # 准备发送的数据
    send_data = input("请输入客户端输入要发送的数据")
    client_socket.send(send_data.encode('utf-8'))

    # 判断
    if send_data == 'bye':
        break

    # 接收一条数据
    info = client_socket.recv(1024).decode('utf-8')
    print("接收到服务器的响应数据：",info)

# 4 关闭socket对象
client_socket.close()










