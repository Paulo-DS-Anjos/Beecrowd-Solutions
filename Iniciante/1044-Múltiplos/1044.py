# -*- coding: utf-8 -*-
A,B = map(int,input().split())
if B > A:
    A,B = B,A
if A % B == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')