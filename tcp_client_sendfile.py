# -*- coding:utf-8 -*-
"""
客户端向服务器发送数据，并请求下载文件
"""
from socket import *
import base64


def sand_file(tcpCliSock):
    # 首先获取发送文件的名称
    sand_file_name = input('请输入要发送的文件名： ')
    # 将要发送的文件名称发送给服务器
    tcpCliSock.send(sand_file_name.encode('utf-8'))
    # 发送文件
    with open(sand_file_name, 'rb') as f:  # 打开文件
        # for line in f:
        #     base64_line = base64.b64encode(line)
        #     tcpCliSock.send(base64_line)
        file_data = f.read()
        base64_data = base64.b64encode(file_data)
        tcpCliSock.send(base64_data)
    return 1


def main():
    server_ip = '192.168.1.2'
    server_port = 8080
    buffer_size = 1024
    server_addr = (server_ip, server_port)

    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(server_addr)  # 连接到服务器地址

    # 发送文件
    sand_result = sand_file(tcpCliSock)
    if sand_result == 1:
        print('文件发送成功')
    recv_data, _ = tcpCliSock.recvfrom(buffer_size)  # recvfrom为元组，将其拆包
    print(recv_data.decode('utf-8'))


if __name__ == '__main__':
    main()
