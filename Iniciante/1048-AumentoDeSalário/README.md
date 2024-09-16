# 1048 - Aumento de Salário

## [Descrição](https://www.beecrowd.com.br/judge/pt/problems/view/1048)

A empresa ABC resolveu conceder um aumento de salários a seus funcionários de acordo com a tabela abaixo:

| Salário | Percentual de Reajuste |
| -- | -- | 
| 0 - 400.00 | 15% |
| 400.01 - 800.00 | 12% |
| 800.01 - 1200.00 | 10% |
| 1200.01 - 2000.00 | 7% |
| Acima de 2000.00 | 4% |

Leia o salário do funcionário e calcule e mostre o novo salário, bem como o valor de reajuste ganho e o índice reajustado, em percentual.

### Entrada:
A entrada contém apenas um valor de ponto flutuante, com duas casas decimais.

### Saída:
Imprima 3 linhas na saída: o novo salário, o valor ganho de reajuste (ambos devem ser apresentados com 2 casas decimais) e o percentual de reajuste ganho, conforme exemplo abaixo.

## Solução

Usar uma variável apenas para o percentual de reajuste ajuda a gente a arrumar melhor o raciocínio necessário para resolver esse problema.

## Python 3.9

```Python
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
```
