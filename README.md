##This is a simple Python 3 multi-threadedserver implementation.
You must have python 3 installed and on your path. To do this you can use
```bash
chmod u+x compile.sh
./compile.sh
```
WARNING, THIS WILL TAKE A WHILE.

When you want to run the server use
```bash
start.sh <portnumber>
```

You can connect to the server via port 3000 and send it commands using
the given cli.py client code that is also included

```bash
python3 cli.py "HELO text\n"
``` 
will cause the server to print out the ip, port number and my student number

```bash
python3 cli.py "KILL_SERVICE\n" will cause the service to exit
```

and other command will be ignored. This server can have 8 active threads to
deal with requests at once. This can be changed my altering the num_threads
variable in the server.py code.
