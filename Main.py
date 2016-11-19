import socket
import sys
import os
import threading
import queue
from server import server


def main():
    my_server = server(str(sys.argv[1]), str(sys.argv[2]))


if __name__ == "__main__":
    main()
