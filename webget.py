#仓库地址
#https://github.com/xiaoshen02/computer-network
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
s.close()
headers,body=data.split(b"\r\n\r\n",1)#以空行为依据分离响应头和响应体
lines=headers.split(b"\r\n")#以换行符为依据分离响应头的每一行
status_code=lines[0].split()[1].decode()#按照空格分隔获取响应状态码
print("状态码:",status_code)
print("响应头:")
for line in lines[1:]:
    print(line)
f=open("resp.bin","wb")#以二进制写入模式
f.write(body)#把body写入文件
f.close()
print(data[:200])