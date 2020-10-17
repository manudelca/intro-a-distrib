import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind((socket.gethostname(), 8080))

sock.listen(5)

while True:

    conn, addr = sock.accept()
    if not conn:
        break
    while True:
        data = conn.recv(1024)
        if len(data) <= 0:
            break
        conn.send(data)


sock.close()

