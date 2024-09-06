# 1009 - Salário com Bônus

## [Descrição](https://www.beecrowd.com.br/judge/pt/problems/view/1009)

Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o total a receber no final do mês, com duas casas decimais.

### Entrada:
O arquivo de entrada contém um texto (primeiro nome do vendedor) e 2 valores de dupla precisão (double) com duas casas decimais, representando o salário fixo do vendedor e montante total das vendas efetuadas por este vendedor, respectivamente.

### Saída:
Imprima o total que o funcionário deverá receber, conforme exemplo fornecido.

## Solução

A compensação do trabalho que o vendedor vai receber ao final das vendas equivale ao salário fixo dele mais 15% das vendas efetuadas por ele. Com isso, basta fazer o cálculo equivalente e imprimir o resultado.

Perceba que o nome do funcionário não é usado para nada, mas é preciso lê-lo mesmo assim. Basta pegar o valor para a variável e não a utilizar mais.

## Python 3.9

```Python
# -*- coding: utf-8 -*-
nome_vendedor = input()
salario_fixo = float(input())
valor_vendas = float(input())
print(f'TOTAL = R$ {(salario_fixo + valor_vendas*0.15):.2f}')
```
