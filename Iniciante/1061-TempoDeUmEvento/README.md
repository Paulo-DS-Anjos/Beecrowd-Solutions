# 1061 - Tempo de um Evento

## [Descrição](https://www.beecrowd.com.br/judge/pt/problems/view/1061)

Pedrinho está organizando um evento em sua Universidade. O evento deverá ser no mês de Abril, iniciando e terminando dentro do mês. O problema é que Pedrinho quer calcular o tempo que o evento vai durar, uma vez que ele sabe quando inicia e quando termina o evento.

Sabendo que o evento pode durar de poucos segundos a vários dias, você deverá ajudar Pedrinho a calcular a duração deste evento.

### Entrada:
Como entrada, na primeira linha vai haver a descrição “Dia”, seguido de um espaço e o dia do mês no qual o evento vai começar. Na linha seguinte, será informado o momento no qual o evento vai iniciar, no formato hh : mm : ss. Na terceira e quarta linha de entrada haverá outra informação no mesmo formato das duas primeiras linhas, indicando o término do evento.

### Saída:
Na saída, deve ser apresentada a duração do evento, no seguinte formato:

W dia(s)
X hora(s)
Y minuto(s)
Z segundo(s)

> Obs: Considere que o evento do caso de teste para o problema tem duração mínima de 1 minuto.

## Solução

Vide problema [1047 - Tempo de Jogo com Minutos](../1047-TempoDeJogoComMinutos).

## Python 3.9

```Python
# -*- coding: utf-8 -*-
def converte(dia, hora, minuto, segundo):
    return (24 * 60 * 60) * dia + (60 * 60) * hora + 60 * minuto + segundo

d_inicial = int(input().split(' ')[1])
h_inicial, m_inicial, s_inicial = [int(x) for x in input().split(' : ')]
d_final = int(input().split(' ')[1])
h_final, m_final, s_final = [int(x) for x in input().split(' : ')]

inicial = converte(d_inicial, h_inicial, m_inicial, s_inicial)
final = converte(d_final, h_final, m_final, s_final)

duracao = final - inicial

print(f'{duracao//(24 * 60 * 60)} dia(s)')
duracao %= (24 * 60 * 60)
print(f'{duracao//(60 * 60)} hora(s)')
duracao %= (60 * 60)
print(f'{duracao//60} minuto(s)')
duracao %= 60
print(f'{duracao} segundo(s)')
```
