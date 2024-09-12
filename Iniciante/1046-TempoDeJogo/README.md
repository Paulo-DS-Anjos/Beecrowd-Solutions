# 1046 - Tempo de Jogo

## [Descrição](https://www.beecrowd.com.br/judge/pt/problems/view/1046)

Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo, sabendo que o mesmo pode começar em um dia e terminar em outro, tendo uma duração mínima de 1 hora e máxima de 24 horas.

### Entrada:
A entrada contém dois valores inteiros representando a hora de início e a hora de fim do jogo.

### Saída:
Apresente a duração do jogo conforme exemplo abaixo.

## Solução

Problema bem simples de resolver depois que entendemos a lógica dele, para calcular a duração do jogo só precisamos subtrair a hora final - a hora inicial do jogo, note que existem casos que o horário final é igual ou menor que o inicial, nesses casos você só precisa acrescentar 24 horas ao horário final já que "ele está um dia a frente"

### Python 3.9

```Python
hora_inicial, hora_final = map(int,input().split())
if(hora_final <= hora_inicial):
    hora_final += 24
print(f'O JOGO DUROU {hora_final - hora_inicial} HORA(S)')
```
