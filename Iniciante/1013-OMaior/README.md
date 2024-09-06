# 1013 - O Maior

## [Descrição](https://www.beecrowd.com.br/judge/pt/problems/view/1013)

Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”. Utilize a fórmula:

<img src="https://latex.codecogs.com/png.image?\dpi{110}\bg{white}&space;MaiorAB=\frac{(A+B+abs(AB))}{2}" title="\bg_white MaxAB"/>

Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b). Um segundo passo, portanto é necessário para chegar no resultado esperado.

### Entrada:
O arquivo de entrada contém três valores inteiros.

### Saída:
Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".

## Solução

Uma forma de conseguir o maior de três elementos usando uma função que só aceita dois elementos é fazer uma composição da seguinte forma:

<img src="https://latex.codecogs.com/png.image?\dpi{110}&space;\bg_white&space;max(a,&space;max(b,&space;c))" title="\bg_white max(a, max(b, c))" />

Com isso, o `max(b, c)` de dentro vai ser executado primeiro, trazendo o maior entre os números `b` e `c`; e depois vai ser executado o `max` de fora, onde vai ser escolhido o máximo entre `a` e o máximo escolhido entre `b` e `c` antes.

### Por que a fórmula funciona?

Considerando que a é o maior número e b é o menor, temos que

<img src="https://latex.codecogs.com/png.image?\dpi{110}&space;\bg_white&space;max(a,&space;b)&space;=&space;\frac{a&space;&plus;&space;b&space;&plus;&space;abs(a&space;-&space;b)}{2}&space;\\\text{}\\max(a,&space;b)&space;=&space;\frac{a&space;&plus;&space;b&space;&plus;&space;a&space;-&space;b}{2}&space;\\\text{}\\max(a,&space;b)&space;=&space;\frac{2a}{2}&space;\\\text{}\\max(a,&space;b)&space;=&space;a" title="\bg_white max(a, b) = \frac{a + b + abs(a - b)}{2} \\\text{}\\max(a, b) = \frac{a + b + a - b}{2} \\\text{}\\max(a, b) = \frac{2a}{2} \\\text{}\\max(a, b) = a" />

como queríamos demonstrar.

O problema pode ser resolvido de duas maneiras diferentes, uma delas é usando o método lambda que cria uma função anônima, ela é tipicamente usada para definir funções pequenas e simples, especialmente quando você precisa de uma função temporária que será usada apenas uma vez ou por pouco tempo. Outra maneira é utilizar a fómula uma vez para encontra o maior valor entre `a` e `b`, armazenar e resultado em uma variável `x` e depois disso realizar uma segunda verificação e `x` (maior valor entre `a` e `b`) e `c`, e então imprimir esse resultado.

## Python 3.9

### Método 1

```Python
# -*- coding: utf-8 -*-
A,B,C = map(int,input().split())
maior = lambda A, B: (A + B + abs(A - B))//2
print(f'{maior(A, maior(B, C))} eh o maior')
```

### Método 2

```Python
# -*- coding: utf-8 -*-
A,B,C = map(int,input().split())
MaiorAB = (A + B + abs(A-B))/2
Maior = (MaiorAB + C + abs(MaiorAB-C))/2
print(f'{Maior:.0f} eh o maior')
```
