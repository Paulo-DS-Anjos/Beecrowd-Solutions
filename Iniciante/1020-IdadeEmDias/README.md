# 1020 - Idade em Dias

## [Descrição](https://www.beecrowd.com.br/judge/pt/problems/view/1020)

Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias

Obs.: apenas para facilitar o cálculo, considere todo ano com 365 dias e todo mês com 30 dias. Nos casos de teste nunca haverá uma situação que permite 12 meses e alguns dias, como 360, 363 ou 364. Este é apenas um exercício com objetivo de testar raciocínio matemático simples.

### Entrada:
O arquivo de entrada contém um valor inteiro.

### Saída:
Imprima a saída conforme exemplo fornecido.

## Solução

Vide [1019 - Conversão de Tempo](../1019-ConversãoDeTempo).

### Python 3.9

```Python
# -*- coding: utf-8 -*-
idade_dias = int(input())

print(f'{idade_dias // 365} ano(s)')
idade_dias %= 365
print(f'{idade_dias // 30} mes(es)')
print(f'{idade_dias % 30} dia(s)')
```
