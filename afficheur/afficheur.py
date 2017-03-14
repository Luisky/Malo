import socket, sys, struct, time


class Afficheur:

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.socket = 0
        self.trame_demande = " "
        self._connection()

    def _connection(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.socket.connect((self.ip, self.port))
        except OSError as m:
            self.socket.close()
            print("error no connection {}".format(m))
            sys.exit(1)

    def _trame(self, mess):
        self.trame_demande = struct.pack('13B', 0x00, 0x00, 0x00, 0x00, 0x00, int(len(mess)+7), 0x01, 0x10, 0x00, 0x01, 0x00, int(len(mess)/2), int(len(mess)))

    def msg(self, message):
        mess = self._msgSet(message)
        self._trame(mess)
        self.trame_demande += self._encode(mess)
        self._write()
        print(self.trame_demande)

    def _encode(self, msg):
        if not type(msg) == bytes:
            return msg.encode()
        else:
            return msg

    def _write(self):
        self.socket.send(self.trame_demande)
        print("send")
        self.socket.close()

    def clean(self, line=0):
        if line == 0:
            self.msg(" "*100)
        else:
            self.msg(" "*20*line)

    def _msgSet(self, msg):
        if len(msg) > 100:
            msg = msg[:100]
        return msg

