import socket
import os

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = int(os.environ.get("PORT"))
sock.bind(('0.0.0.0', port))
sock.listen(5)

while True:
    print("Waiting connection on port {}".format(port))
    conn, addr = sock.accept()
    print("Conection accepted!")
    if not conn:
        break
    while True:
        data = conn.recv(1024)
        print(data.decode())
        if len(data) <= 0:
            break
        conn.send(data)


sock.close()

