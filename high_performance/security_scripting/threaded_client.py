import socket
import threading


class ClientConnect(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    
    def run(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        addr = ("www.google.com", 443)
        sock.connect(addr)
        print("connected")

sock_clients = []
for i in range(1, 100):
    s = ClientConnect()
    s.start()
    print("started:", i)
    sock_clients.append(s)