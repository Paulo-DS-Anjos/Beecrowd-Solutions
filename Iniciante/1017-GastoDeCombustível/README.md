# 1017 - Gasto de Combustível

## [Descrição](https://www.beecrowd.com.br/judge/pt/problems/view/1017)

Joaozinho quer calcular e mostrar a quantidade de litros de combustível gastos em uma viagem, ao utilizar um automóvel que faz `12 KM/L`. Para isso, ele gostaria que você o auxiliasse através de um simples programa. Para efetuar o cálculo, deve-se fornecer o `tempo gasto na viagem (em horas)` e a `velocidade média durante a mesma (em km/h)`. Assim, pode-se obter distância percorrida e, em seguida, calcular quantos litros seriam necessários. Mostre o valor com 3 casas decimais após o ponto.

### Entrada:
O arquivo de entrada contém dois inteiros. O primeiro é o `tempo gasto na viagem (em horas)` e o segundo é a `velocidade média durante a mesma (em km/h)`.

### Saída:
Imprima a quantidade de litros necessária para realizar a viagem, com três dígitos após o ponto decimal

## Solução

A resolução desse problema envolve duas etapas:

1. Calcular a distância percorrida pelo carro, que pode ser calculada `multiplicando` a `velocidade (em km/h)` pelo `tempo (em horas)`;
2. Como o carro faz `12 km/L`, pegar a `distância percorrida (em km)` e `dividir` por `12 (km/L)` para descobrir quantos litros precisa para percorrer a viagem no tempo e velocidade passados.

### Python
```Python
# -*- coding: utf-8 -*-
tempo = float(input())
velocidade_media = float(input())
distancia = tempo * velocidade_media
gasto = distancia / 12
print(f'{gasto:.3f}')
```
