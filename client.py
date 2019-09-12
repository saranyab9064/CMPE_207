import socket

TCP_IP = '94.142.241.111'
TCP_PORT = 23
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
while (True):
    data = s.recv(BUFFER_SIZE)
    print ("received data:", data)