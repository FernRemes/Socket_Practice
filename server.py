import socket
import threading

HEADER = 1024
PORT = 8000
# SERVER = "127.0.0.1"
SERVER = socket.gethostbyname(socket.gethostname()) # soft code get the ip of the network device
ADDR = (SERVER, PORT)
DISCONNECT_MSG = "!DISCONNECT"
# print(SERVER) # print server ip
# print(socket.gethostname()) # print name computer address

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create a socket stream
server.bind(ADDR)

def handle_client(conn, addr):
    print("NEW CONNECTION", addr, "connected")

    connected = True

    while connected:
        msg_len = conn.recv(HEADER).decode("utf-8")
        if msg_len:
            msg_len = int(msg_len)
            msg = conn.recv(msg_len).decode("utf-8")

            if msg == DISCONNECT_MSG:
                connected = False
            print(f"[{addr}]: {msg}")

            conn.send("MSG received ".encode("utf-8"))
    
    conn.close()
    


def start():
    server.listen()
    while(True):
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args = (conn, addr))
        thread.start()

        print("Active connections: ", threading.activeCount() - 1)

print("Starting server ... ")
start()


