#============================================================================
# Name        : TCP_Server.py
# Author      : Saranya Balakrishnan
# SJSU ID     : 013786097
#============================================================================


import socket

def tcp_server():
    # get the hostname
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024
    # get instance and create a socket
    server_socket = socket.socket()
    # bind host address and port together
    server_socket.bind((host, port))

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    # accept new connection
    conn, addr = server_socket.accept()
    print("Connection from: " + str(addr))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        print("from connected user: " + str(host))
        data = input(' -> ')
        # send data to the client
        conn.send(data.encode())
        # close the connection
    conn.close()

if __name__ == '__main__':
    tcp_server()