import socket 
import sys
from time import sleep
from models import Request

HOST = 'localhost'
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST, PORT))

print('Connected')

for i in range(3):
    if i == 0:
        request = Request(
            path='/',
            method='GET',
            headers=['Connection: Keep-Alive']
        )
    else:
        request = Request(
            path='/',
            method='POST'
        )

    message =request.build()

    s.send(message.encode('ascii'))

    response = s.recv(1024).decode('ascii')

    print(response)

    sleep(1)

sleep(5)