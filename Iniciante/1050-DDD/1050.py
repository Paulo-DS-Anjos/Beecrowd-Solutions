# -*- coding: utf-8 -*-
dicionario = {
    61 : 'Brasilia',
    71 : 'Salvador',
    11 : 'Sao Paulo',
    21 : 'Rio de Janeiro',
    32 : 'Juiz de Fora',
    19 : 'Campinas',
    27 : 'Vitoria',
    31 : 'Belo Horizonte',
    }

ddd = int(input())
print('DDD nao cadastrado' if not ddd in dicionario else dicionario[ddd])