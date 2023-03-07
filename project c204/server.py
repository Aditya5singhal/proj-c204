
import socket
from  threading import Thread

SERVER = None
PORT = 6000
IP_ADDRESS = '127.0.0.1'

CLIENTS = {}




def acceptConnections():
    global CLIENTS
    global SERVER

    while True:
        player_socket, addr = SERVER.accept()
        
        playerName=player_socket.recv(1024).decode().strip()
        
        if(len(CLIENTS.keys())==0):
            CLIENTS[playerName]={"playerType":"player1"}
        else:
            CLIENTS[playerName]={"playerType":"player2"}
            
        CLIENTS[playerName]["player_socket"]=player_socket
        CLIENTS[playerName]["address"]=addr
        CLIENTS[playerName]["playerName"]=playerName
        CLIENTS[playerName]["turn"]=False
        
        print(f"connection established{playerName}:{addr}")
        

        






def setup():
    print("\n")
    print("\t\t\t\t\t\t*** WELCOME TO THE TAMBOLA GAME ***")


    global SERVER
    global PORT
    global IP_ADDRESS

    IP_ADDRESS = '127.0.0.1'
    PORT = 5000
    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS, PORT))

    SERVER.listen(10)

    print("\t\t\t\tSERVER IS WAITING FOR INCOMMING CONNECTIONS...")
    print("\n")

    acceptConnections()


setup()
