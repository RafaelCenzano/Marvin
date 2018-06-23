#!/bin/bash

set -x
source ~rafael/.bashrc
echo $PATH
workon marvin

python2.7 /home/rafael/Documents/Programming/Marvin-Jarvis-/marvin_code.py
