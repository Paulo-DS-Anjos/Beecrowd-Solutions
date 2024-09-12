# -*- coding: utf-8 -*-
hora_inicial,minuto_inicial,hora_final,minuto_final = map(int,input().split())
final = hora_final * 60 + minuto_final
inicial = hora_inicial * 60 + minuto_inicial
if final <= inicial:
    final += 24 * 60
print(f'O JOGO DUROU {(final - inicial)//60} HORA(S) E {(final - inicial)%60 } MINUTO(S)')
