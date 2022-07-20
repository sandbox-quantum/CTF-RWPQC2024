import socket
from tlslite.api import *

def main():

    address = ("35.196.160.7", 4433)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)
    sock.connect(address)
    sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    connection = TLSConnection(sock)

    settings = HandshakeSettings()
    connection.handshakeClientCert(None, None,
        settings=settings)
    print("Handshake success")

    connection.send(b"GET /flag HTTP/1.1\r\nHost: localhost\r\nUserAgent: ctf-client\r\n\r\n")
    data = b""
    while True:
        try:
            r = connection.recv(1024)
            if not r:
                break
            data += r
        except socket.timeout:
            break
        except TLSAbruptCloseError:
            break
    print("Received data: ", data.decode())

if __name__ == '__main__':
    main()
