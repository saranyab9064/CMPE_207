#============================================================================
# Name        : TCP_Server.py
# Author      : Saranya Balakrishnan
# SJSU ID     : 013786097
#============================================================================

import socket
import pyfiglet
def tcp_server():
    # get the hostname
    host = socket.gethostname()
    port = 1234  # initiate port no above 1024
    # get instance and create a socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # bind host address and port together
    s.bind((host, port))
    # configure how many client the server can listen simultaneously
    s.listen(5)

    while True:
        # now our endpoint knows about the OTHER endpoint.
        clientsocket, address = s.accept()
        # Connection established successfully to the client
        print(f"Connection from {address} has been established.")
        # send the message to client in ascii art format
        ascii_banner = pyfiglet.figlet_format("Hello World")
        clientsocket.send(bytes(ascii_banner,"utf-8"))
        clientsocket.close()

if __name__ == '__main__':
    tcp_server()