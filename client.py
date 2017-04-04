import socket, struct,sys
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect(("", 1996))
#msg = struct.pack('1B', 0x10)
#msg += "alloav8".encode()
#s.send(msg)
#s.close()
#print("data send")

class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.socke = 0
        self._connection()
        self.trame = ""

    def _connection(self):
        self.socke = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            self.socke.connect((self.ip,self.port))
        except OSError as error:
            self.socke.close()
            print("error ", error)
            sys.exit(-1)

    def _settrame(self, code_fonc ,id =""):
        id += code_fonc
        self.trame = id

    def initialisation(self,long,lat,text):

