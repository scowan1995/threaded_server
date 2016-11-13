#!/bin/bash

wget https://www.python.org/ftp/python/3.5.2/Python-3.5.2rc1.tgz 
tar xvzf Python-3.5.2rc1.tgz 
cd Python-3.5.2rc1
./configure
make
make altinstall prefix=~/local
ln -s ~/local/bin/python3.5.2 ~/local/bin/python
