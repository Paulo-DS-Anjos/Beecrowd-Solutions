# -*- coding: utf-8 -*-
idade_dias = int(input())

print(f'{idade_dias // 365} ano(s)')
idade_dias %= 365
print(f'{idade_dias // 30} mes(es)')
print(f'{idade_dias % 30} dia(s)')