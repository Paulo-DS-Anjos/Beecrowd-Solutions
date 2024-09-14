# 1049 - Animal

## [Descrição](https://www.beecrowd.com.br/judge/pt/problems/view/1049)

Neste problema, você deverá ler 3 palavras que definem o tipo de animal possível segundo o esquema abaixo, da esquerda para a direita.  Em seguida conclua qual dos animais seguintes foi escolhido, através das três palavras fornecidas.

![1049 - Beecrowd](https://resources.beecrowd.com/gallery/images/problems/UOJ_1049_b.png)

### Entrada:
A entrada contém 3 palavras, uma em cada linha, necessárias para identificar o animal segundo a figura acima, com todas as letras minúsculas.

### Saída:
Imprima o nome do animal correspondente à entrada fornecida.

## Solução

Eu acho esse problema super legal para testar seu conhecimento de estruturas condicionais (`if`), mas as soluções em JavaScript e Python mostram outra abordagem muito interessante com dicionários. É possível implementar essa solução em C++, C# e Java também, fica a seu critério. Abaixo está a solução utilizando os dois métodos citados.

## Python 3.9

### Método 1:

```Python
# -*- coding: utf-8 -*-
p1 = input()
p2 = input()
p3 = input()

if p1 == 'vertebrado':
    if p2 == 'ave':
        if p3 == 'carnivoro':
            print('aguia')
        elif p3 == 'onivoro':
            print('pomba')
    elif p2 == 'mamifero':
        if p3 == 'onivoro':
            print('homem')
        elif p3 == 'herbivoro':
            print('vaca')
elif p1 == 'invertebrado':
    if p2 == 'inseto':
        if p3 == 'hematofago':
            print('pulga')
        elif p3 == 'herbivoro':
            print('lagarta')
    elif p2 == 'anelideo':
        if p3 == 'hematofago':
            print('sanguessuga')
        elif p3 == 'onivoro':
            print ('minhoca')
```

### Método 2:

```Python
arvore = {
    "vertebrado": {
        "ave": {
            "carnivoro": "aguia",
            "onivoro": "pomba"
        },
        "mamifero": {
            "onivoro": "homem",
            "herbivoro": "vaca"
        }
    },
    "invertebrado": {
        "inseto": {
            "hematofago": "pulga",
            "herbivoro": "lagarta"
        },
        "anelideo": {
            "hematofago": "sanguessuga",
            "onivoro": "minhoca"
        }
    }
}

caracteristicas = []

for _ in range(3):
    caracteristicas.append(input())

print(arvore[caracteristicas[0]][caracteristicas[1]][caracteristicas[2]])
```
