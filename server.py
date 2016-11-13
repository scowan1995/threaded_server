""" 
A simple echo server 
""" 

import socket 
import sys
import os
import threading
import random
import time
import queue

num_threads = 8
host = ''
port = sys.argv[1]
 
def get_msg(string):
    msg_list = []
    for i in string[4:]:
        msg_list.append(i)
    return "".join(msg_list)

def get_my_IP():
    return socket.gethostbyname(socket.gethostname())

def handle_helo(client, msg):
    reply_msg = "HELO"+msg+"IP:"+ get_my_IP() +"\nPort:"+str(port)+"\nStudentID:13325878\n"
    print(reply_msg)
    client.send(reply_msg.encode("utf-8"))
    return reply_msg

def handle_other():
    print("handled useless request")

def handle_kill():
    os._exit(0)

def do_a_thing(que):
    while 1:
        print("loop in do_a thing")
        f = que.get()
        f[0](f[1],f[2]) #call handle with client, address
        print("handled")
        que.task_done()

def handle(client, address):
    pack_size = 1024
    data = client.recv(pack_size)
    decoded_data = data.decode("utf-8")
    print("handling another thing")
    print("decoded data: "+decoded_data)
    if decoded_data[:4]  == "HELO" :
        msg = get_msg(decoded_data)
        handle_helo(client, msg)
        handle(client, address)
    elif decoded_data[:12] == "KILL_SERVICE":
        print("killing")
        handle_kill()
    else:
       handle_other() 
       handle(client, address)


def main():
    backlog = 5
    size = 1024
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, int(port)))
    s.listen(backlog)
    q = queue.Queue(maxsize=num_threads)
    for i in range(num_threads):
        threading.Thread(target=do_a_thing, args=(q,)).start()

    while 1:
        client, address = s.accept()
        print("accepting")
        q.put((handle, client, address))

    
if __name__=="__main__":
    main()
