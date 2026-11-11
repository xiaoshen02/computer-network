#仓库地址
#https://github.com/xiaoshen02/computer-network
import socket 
import sys
#判断参数
if(len(sys.argv)<3):
    print("用法：python webget.py host path [port]")
    sys.exit(1)
host=sys.argv[1]
path=sys.argv[2]#获取参数
if len(sys.argv)>=4:#获取端口
    port=int(sys.argv[3])
else:
    port=80
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#超时时间为10秒
s.settimeout(10)
#连接服务器
s.connect((host, port))
#发送请求
request = (
        f"GET {path} HTTP/1.1\r\n"
        f"Host: {host}\r\n"
        f"Connection: close\r\n"
        f"\r\n"
    )

s.sendall(request.encode())
data=b""
count=0
while True:
    message=s.recv(1024)
    count+=1
    print("第", count, "次接收数据", len(message), "字节")
    if not message:#没收到数据说明连接关闭
        break
    data+=message
print("recv总调用次数：",count)
s.close()
headers,body=data.split(b"\r\n\r\n",1)#以空行为依据分离响应头和响应体
lines=headers.split(b"\r\n")#以换行符为依据分离响应头的每一行
status_code=lines[0].split()[1].decode()#按照空格分隔获取响应状态码
print("状态码:",status_code)
print("响应头:")
for line in lines[1:]:
    print(line.decode("utf-8"))
f=open("resp.bin","wb")#以二进制写入模式
f.write(body)#把body写入文件
f.close()
print(data[:200])