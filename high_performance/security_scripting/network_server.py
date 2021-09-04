import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind(('', 5001))
sock.listen(5)

c, addr = sock.accept()
data = c.recv(512)

if data:
    print("connection frm ", addr[0], data)
