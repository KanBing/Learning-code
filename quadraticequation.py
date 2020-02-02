#!/usr/bin/env python3
import math
a = int(input("please input a: "))
b = int(input("please input b: "))
c = int(input("please input c: "))
d = b*b-4*a*c

if d<0:
    print("no value")
else:
    root1 = (-b + math.sqrt(d))/(2*a)
    root2 = (-b - math.sqrt(d))/(2*a)
    print("root 1 ={:.2f}".format(root1))
    print("root 2 ={:.2f}".format(root2))


