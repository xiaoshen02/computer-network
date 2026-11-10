import socket 
s=socket.socket(socket.AF_NET,socket.SOCK_STREAM)
s.connct(("www.bjfu.edu.cn",80))
s.sendall(b"GET / HTTP/1.1\r\nHost: www.bjfu.edu.cn\r\n\r\n")
data=s.recv(1024)
print(data[:200])