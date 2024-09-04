# -*- coding: utf-8 -*-
cod_1,num_pecas1,valor_peca1 = map(float,input().split())
cod_2,num_pecas2,valor_peca2 = map(float,input().split())
print(f'VALOR A PAGAR: R$ {(num_pecas1*valor_peca1 + num_pecas2*valor_peca2):.2f}')