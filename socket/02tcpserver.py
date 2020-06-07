import socket

HOST = "10.10.10.234"
POST = 5000
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
addr = (HOST,POST)

def main(addr):
    s.bind(addr)
    s.listen(1)
    conn,addr = s.accept()
    print(addr)
    while True:
        data = conn.recv(1024)
        print(data)
        if data == b"quit":
            break
        conn.send(data.upper())

    conn.close()
    s.close()

if __name__ == "__main__":
    main(addr)
