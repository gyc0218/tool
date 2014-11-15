import socket

serAddr = ('192.168.1.100', 9999)


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(serAddr)
    sock.listen(5)
    
    while True:
        conn, clientAddr = sock.accept()

        try:
            while True:
                recvData = conn.recv(16)
                if recvData:
                    print clientAddr,'---ask----',recvData
                    conn.sendall('I am gaoyongcai')
                else:
                    print clientAddr,'not  say anything'
                    break
        finally:
            conn.close()
            
