# 1042 - Sort Simples

## [Descrição](https://www.beecrowd.com.br/judge/pt/problems/view/1042)

Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os valores em ordem crescente, uma linha em branco e em seguida, os valores na sequência como foram lidos.

### Entrada:
A entrada contem três números inteiros.

### Saída:
Imprima a saída conforme foi especificado.

## Solução

Podemos simplesmente colocar estes valores em um vetor e ordená-los usando o método naturalmente de ordenação ou usando métodos de ordenação.
> Seja qual for a solução, lembre-se de guardar a ordem original da entrada em outras variáveis.

### Método 1 - Transformando em vetor e ordenando com `sort()`

Esta abordagem é mais simples, só é um pouco menos performática, mas a diferença é bem pouquinha mesmo.

### Método 2 - Usando InsertionSort

Um método eficiente e fácil de implementar que podemos usar é o InsertionSort, onde podemos proceder da seguinte maneira:

1. Verificar se o segundo elemento é menor que o primeiro. Se for, trocar as posições de ambos;
2. Verificar se o terceiro elemento é menor que o segundo. Se for, trocar as posições de ambos;
3. Se no passo anterior, se os elementos foram trocados, então verificar novamente se o agora segundo elemento é menor que o primeiro e se for, trocar as posições de ambos.

## Python 3.9

### Método 1:
```Python
V = [int(x) for x in input().strip().split(' ')]
v = V[:]
v.sort()

for i in range(3):
    print(v[i])
print()
for i in range(3):
    print(V[i])
```

### Método 2:

```Python
A, B, C = map(int,input().split())
a, b, c = A, B, C

if(b < a):
    a, b = b, a
if(c < b):
    b, c = c, b
    if(b < a):
        a, b = b, a
print(a)
print(b)
print(c)
print()
print(A)
print(B)
print(C)
```
