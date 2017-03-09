import socket, threading, trame_handler


class ServerThread(threading.Thread):

    def __init__(self, ip, port, clientsocket):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.clientsocket = clientsocket
        print("[+] new thread for %s %s \n" % (self.ip, self.port, ))

    def run(self):
        print("Connection of %s %s \n" % (self.ip, self.port, ))
        trame_handler.DataHandler(self.clientsocket.recv(2048))
        print("Client deconnected")
        self.clientsocket.close()

def serv():
    tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpsocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcpsocket.bind(("",2000))
    while True:
        tcpsocket.listen(10)
        print("Server listening")
        (clientsocket, (ip,port)) = tcpsocket.accept()
        newThread = ServerThread(ip, port, clientsocket)
        newThread.start()
        print(threading.active_count())

if __name__ == "__main__":
    serv()