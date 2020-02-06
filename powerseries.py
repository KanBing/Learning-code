#!/usr/bin/env python3
import math
x = float(input("enter value of x: "))
y = 1
result =0.0
n = 0
while n <= 100000:
    y *= y
    result += (math.pow(x , n))/y
    n += 1
print("No of Times={} and Result= {:10f}".format(n, result))

compare = math.exp(x)
print("math function is:{:.10f}".format(compare))
