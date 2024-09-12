# -*- coding: utf-8 -*-
hora_inicial, hora_final = map(int,input().split())
if(hora_final <= hora_inicial):
    hora_final += 24
print(f'O JOGO DUROU {hora_final - hora_inicial} HORA(S)')