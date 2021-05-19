from __future__ import print_function
import os
import shutil
from libs.detect import detect
import time
input_path = "input"
output_path = "output"
dir = "./out/run/labels/"
weights = "best.pt"

# Do the digit recognition of input file
while True:
    f = input()
    try:
        shutil.rmtree("./out")
    except:
        pass
    try:
        detect(f,weights,0.5)
        txtpath = os.listdir(dir)[0]
        txt = open(dir + txtpath ,mode = 'r')
        data = txt.read()
        txt.close()

        data = str(data.split("\n")[:-1])
    except OSError as e:
        print(e)
    try:
        shutil.rmtree("./out")
    except:
        pass
    print("IN: " + f)
    print("OUT: " + data)

