import socket
import os
port = 12000
buf=1024


print("Done")
while True:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(("",10000))
    s.listen(1)
    conn, addr = s.accept()
    data = conn.recv(buf)
    if not data: break
    print(data)
    conn.send(data)
    conn.close()
    s.close()
    os.system("python start.py")
    r = int(input())
