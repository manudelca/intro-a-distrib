import socket
import sys

def main():
    port = int(sys.argv[1])
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("wss://tp1-intro-a-distrib.herokuapp.com/0.0.0.0", port))

    sock.send(("Hola!").encode())

    response = sock.recv(1024)

    print(response.decode())

    sock.close()


main()