""" 
A simple echo server 
""" 

import socket 
import os
import threading
import random
import time
import queue

num_threads = 8
host = ''
port = 3001

def get_my_IP():
    return socket.gethostbyname(socket.gethostname())

def handle_helo():
    reply_msg = "HELO txt\nIP:"+ get_my_IP() +"\nPort:"+str(port)+"\nStudentID:13325878\n"
    print(reply_msg)
    return reply_msg

def handle_other():
    pass

def handle_kill():
    os._exit(0)

def do_a_thing(que):
    while 1:
        f = que.get()
        f[0](f[1],f[2]) #call handle with client, address
        que.task_done()

def handle(client, address):
    pack_size = 1024
    data = client.recv(pack_size)
    decoded_data = data.decode("utf-8")
    if decoded_data  == "HELO text\n" :
        handle_helo()
    elif decoded_data == "KILL_SERVICE\n":
        handle_kill()
    else:
        pass


def main():
    backlog = 5
    size = 1024
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(backlog)
    q = queue.Queue(maxsize=8)
    for i in range(num_threads):
        threading.Thread(target=do_a_thing, args=(q,)).start()

    while 1:
        client, address = s.accept()
        q.put((handle, client, address))

    
if __name__=="__main__":
    main()