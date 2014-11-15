import socket

serAddr = ('192.168.1.100', 9999)


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(serAddr)

    try:
        message = 'hello word'
        sock.sendall(message)

        recvData = sock.recv(16)
        print recvData

    finally:
        sock.close()
