#!/bin/bash

for f in *.py
do
    echo "Sending $f to $HOST..."
    python webrepl/webrepl_cli.py -p $PASSWD $f $HOST:$f 
    echo "Done."
done