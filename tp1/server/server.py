import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind(('0.0.0.0', 8080))
sock.listen(5)

while True:
    print("Waiting connection...")
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

