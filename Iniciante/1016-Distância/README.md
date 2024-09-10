# 1016 - Distância

## [Descrição](https://www.beecrowd.com.br/judge/pt/problems/view/1016)

`Dois carros (X e Y)` partem em uma mesma direção. O carro `X` sai com velocidade constante de `60 Km/h` e o carro `Y` sai com velocidade constante de `90 Km/h`.

Em uma hora (`60 minutos`) o carro `Y` consegue se distanciar `30 quilômetros` do carro `X`, ou seja, consegue se afastar `um quilômetro a cada 2 minutos`.

Leia a distância (`em Km`) e calcule quanto tempo leva (`em minutos`) para o carro `Y` tomar essa distância do outro carro.

### Entrada:
O arquivo de entrada contém um número inteiro.

### Saída:
Imprima o tempo necessário seguido da mensagem `minutos`.

## Solução

No enunciado, está dizendo que o carro `Y` se distancia do carro `X` um quilômetro a cada `2 minutos`. Logo, cada quilômetro de distância significa 2 minutos que se passaram.

## Python 3.9

```Python
# -*- coding: utf-8 -*-
x= int(input())
print(f'{x*2} minutos')
```
