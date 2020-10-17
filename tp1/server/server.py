import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind(("127.0.0.1", 8081))
sock.listen(5)

while True:

    conn, addr = sock.accept()
    if not conn:
        break
    while True:
        data = conn.recv(1024)
        print(data.decode())
        if len(data) <= 0:
            break
        conn.send(data)


sock.close()

