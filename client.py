import socket

HEADER = 1024
PORT = 8000
DISCONNECT_MSG = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname()) # soft code get the ip
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode("utf-8")
    msg_len = len(message)

    send_len = str(msg_len).encode("utf-8")
    send_len += b' ' * (HEADER - len(send_len))

    client.send(send_len)
    client.send(message)
    print(client.recv(HEADER).decode("utf-8"))

send("Hello, world!")
send(DISCONNECT_MSG)
