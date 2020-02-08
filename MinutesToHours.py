#!/usr/bin/env python3
import sys

# define function
def Hours(input_num):
    if input_num < 0:
        raise ValueError("Input number can not be negative")
    else:
        Hour = 0
        minitues = 0
        Hour = (input_num) / 60
        minitues = (input_num) % 60
        print("{} H, {} M".format(int(Hour),int(minitues)))
# call function
try:
    Hours(int(sys.argv[1]))
except:
    print("Parameter Error")


