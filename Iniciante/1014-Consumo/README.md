# 1014 - Consumo

## [Descrição](https://www.beecrowd.com.br/judge/pt/problems/view/1014)

Calcule o consumo médio de um automóvel sendo fornecidos a distância total percorrida (em Km) e o total de combustível gasto (em litros).

### Entrada:
O arquivo de entrada contém dois valores: um valor inteiro X representando a distância total percorrida (em Km), e um valor real Y representando o total de combustível gasto, com um dígito após o ponto decimal.

### Saída:
Apresente o valor que representa o consumo médio do automóvel com 3 casas após a vírgula, seguido da mensagem "km/l".

## Solução

Se queremos saber o consumo médio do automóvel por km/L, precisamos dividir a distância percorrida (em km) pelo total de combustível gasto (em L).

## Python

```Python
# -*- coding: utf-8 -*-
distancia = int(input())
combustivel = float(input())
print(f'{(distancia/combustivel):.3f} km/l')
```
