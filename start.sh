#!/bin/bash

if (python -c 'import sys; print(sys.version_info[:])'[0]==3){
    python Main.py $1
}
else{
    python3 Main.py $1
}
