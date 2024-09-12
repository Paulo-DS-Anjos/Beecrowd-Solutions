# 1047 - Tempo de Jogo com Minutos

## [Descrição](https://www.beecrowd.com.br/judge/pt/problems/view/1047)

Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir calcule a duração do jogo.

`Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.`

### Entrada:
Quatro números inteiros representando a hora de início e fim do jogo.

### Saída:
Mostre a seguinte mensagem: “O JOGO DUROU XXX HORA(S) E YYY MINUTO(S)” .

## Solução

Esse problema é uma mistura dos problemas [1046 - Tempo de Jogo](../1046-TempoDeJogo) e [1019 - Conversão de Tempo](../1019-ConversãoDeTempo).

## Python 3.9

```Python
# -*- coding: utf-8 -*-
hora_inicial,minuto_inicial,hora_final,minuto_final = map(int,input().split())
final = hora_final * 60 + minuto_final
inicial = hora_inicial * 60 + minuto_inicial
if final <= inicial:
    final += 24 * 60
print(f'O JOGO DUROU {(final - inicial)//60} HORA(S) E {(final - inicial)%60 } MINUTO(S)')
```
