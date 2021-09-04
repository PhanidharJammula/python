import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 5000)
mysock.connect(addr)

try:
    msg = b"Hi this is a test"
    mysock.sendall(msg)
except socker.errno as e:
    print("socket error")
finally:
    mysock.close()