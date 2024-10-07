# -*- coding: utf-8 -*-
x = int(input())
for _ in range (x):
    num = int(input())
    if num == 0:
        print('NULL')
    elif num % 2 == 0:
        if num > 0:
            print('EVEN POSITIVE')
        else:
            print('EVEN NEGATIVE')
    else:
        if num > 0:
            print('ODD POSITIVE')
        else:
            print('ODD NEGATIVE')
