import socket 
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#超时时间为10秒
s.settimeout(10)
s.connect(("www.bjfu.edu.cn",80))
s.sendall(b"GET / HTTP/1.1\r\nHost: www.bjfu.edu.cn\r\nConnection: close\r\n\r\n")#加close
data=b""
while True:#循环接收数据
    message=s.recv(1024)
    if not message:#没接收到字节说明服务端已经关闭连接
        break
    data+=message

print(data[:200])