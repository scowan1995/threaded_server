import socket
import sys

host = "localhost"
port = 3001

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    mystring = str(sys.argv[1])
    s.sendall(mystring.encode("utf-8"))

