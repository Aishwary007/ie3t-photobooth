import socket
import os
import time
port = 12000
buf = 1024

print("Started")
while True:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(("",10000))
    s.listen(1)
    print("Listening for the signal...")
    conn, addr = s.accept()
    data = conn.recv(buf)
    if not data: break
    print(data)
    conn.send(data)
    conn.close()
    s.close()
    print("Capturing...")
    os.system("python start.py")
    print("Enter anything to continue...")
    time.sleep(5)
    a = raw_input()
