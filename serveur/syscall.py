class Syscall:

    def __init__(self,trame):
        self.trame = trame
        self._parse()

    def _parse(self):
        if self.trame[1] == 0x02:
            print("reboot")
