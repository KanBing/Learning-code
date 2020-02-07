#!/usr/bin/env python3
n = int(input("enter the num of students: "))
data = {} # used for saving dictionary variable
subjects = ("physics" , "maths" , "history")
for i in range(0 , n):
    name = input("enter the name of the student {}:".format(i+1)) #get the name of students
    marks = []
    for x in subjects:
        marks.append(int(input("enter marks of {}: ".format(x))))
    data[name] = marks
for x, y in data.items():
    total = sum(y)
    print("{}'s total maks is {}".format(x, total))
    if total < 120:
        print(x, "failed")
    else:
        print(x, "passed")
