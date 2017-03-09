import socket, struct
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("", 2000))
msg = struct.pack('1B', 0x10)
msg += "alloav8".encode()
s.send(msg)
s.close()
print("data send")