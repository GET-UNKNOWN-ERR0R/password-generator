#!/bin/bash

if ! command -v python3 &> /dev/null
then
    echo "Python3 is not installed. Please install Python3 to run the program."
    exit
fi

python3 password_generator.py
