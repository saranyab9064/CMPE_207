import socket

TCP_IP = '94.142.241.111'
TCP_PORT = 23
BUFFER_SIZE = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
client, addr = s.accept()
print("[*] Get a connection from", addr[0],":",addr[1])
while 1:
     data = client.recv(BUFFER_SIZE)
     if not data: break
     print ("received data:", data)
     client.send(data)
client.close()
