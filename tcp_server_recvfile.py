import socket
import base64


def main():
    # 创建套接字
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定ip及端口
    tcp_server.bind(('', 7890))
    # 将默认的套接字由主动变为被动接听
    tcp_server.listen(128)
    # while True:
    # 等待客户端的数据
    new_client_socket, client_addr = tcp_server.accept()
    # 接收客户端发送过来的请求
    recv_data_64 = new_client_socket.recv(1024)
    recv_data = base64.b64decode(recv_data_64)  # 解码
    # 将接收到的数据写入到文件中
    fp = open('new1.txt', 'wb+')
    print("数据写入中..")
    fp.write(recv_data)
    new_client_socket.close()
    # 发送数据到客户端
    new_client_socket.send('hello'.encode('utf-8'))
    # 关闭套接字
    new_client_socket.close()
    tcp_server.close()


if __name__ == '__main__':
    main()