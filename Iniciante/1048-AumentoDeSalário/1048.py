# -*- coding: utf-8 -*-
salario = float(input())

if(0 <= salario <= 400.00):
    reajuste = 15
elif(400 < salario <= 800.00):
    reajuste = 12
elif(800 < salario <= 1200.00):
    reajuste = 10
elif(1200 < salario <= 2000.00):
    reajuste = 7
else:
    reajuste = 4

print(f'Novo salario: {salario * (1 + reajuste/100):.2f}')
print(f'Reajuste ganho: {salario * reajuste/100:.2f}')
print(f'Em percentual: {reajuste} %')
