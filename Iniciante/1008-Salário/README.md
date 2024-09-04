# 1008 - Salário

## [Descrição](https://www.beecrowd.com.br/judge/pt/problems/view/1008)

Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas, o valor que recebe por hora e calcula o salário desse funcionário. A seguir, mostre o número e o salário do funcionário, com duas casas decimais.

Entrada
O arquivo de entrada contém 2 números inteiros e 1 número com duas casas decimais, representando o número, quantidade de horas trabalhadas e o valor que o funcionário recebe por hora trabalhada, respectivamente.

Saída
Imprima o número e o salário do funcionário, conforme exemplo fornecido, com um espaço em branco antes e depois da igualdade. No caso do salário, também deve haver um espaço em branco após o $.

## Solução

Para calcular o salário do funcionário, basta multiplicar o valor que ele recebe por hora pelo número de horas trabalhadas. Após isso, imprimir tanto o número do funcionário quanto o salário que calculamos.

## Python

```Python
# -*- coding: utf-8 -*-
num_funcionario = int(input())
num_horas_trabalhadas = int(input())
salario = float(input())
print(f'NUMBER = {num_funcionario}')
print(f'SALARY = U$ {(num_horas_trabalhadas * salario):.2f}')
```
