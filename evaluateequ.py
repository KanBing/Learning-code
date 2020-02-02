#!/usr/bin/env python3
sum = 0
for i in range(1,11):
    sum += 1.0 / i
    print("{:2d} {:10.2f}".format(i,sum,))

