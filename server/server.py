import socket, sys
from daemon import Daemon


class MyDaemon(Daemon):
    def run(self):
        serv()


def serv():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 2000))
    while True:
        print("listening")
        s.listen(5)
        client, address = s.accept()
        print("{} connected".format(address))
        msg(client)


def msg(client):
    while True:
        response = client.recv(255)
        print(response)


if __name__ == "__main__":
    daemon = MyDaemon('/tmp/server-daemon.pid')
    if len(sys.argv) == 2:
        if sys.argv[1] == 'start':
            daemon.start()
        elif sys.argv[1] == 'stop':
            daemon.stop()
        elif sys.argv[1] == 'restart':
            daemon.restart()
        else:
            print("unknow command")
            sys.exit(2)
        sys.exit(0)
    else:
        print("usage %s start|stop|restart" % sys.argv[0])
        sys.exit(2)





