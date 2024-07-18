# -*- coding: utf-8 -*-

X = int(input())

level = 1
Y = X
while True:
    if Y > level:
        Y = Y-level
        level = level+1
    else:
        if level %2 ==0:
            print(Y, "/", level+1-Y, sep = "")
            break
        else:
            print(level+1-Y, "/", Y, sep="")
            break
