# -*- coding: utf-8 -*-
N1,N2,N3,N4 = map(float,input().strip().split())
MEDIA = (N1*2 + N2*3 + N3*4 + N4)/10
print(f'Media: {MEDIA:.1f}')
if 5 <= MEDIA <= 6.9:
    print('Aluno em exame.')
    NOTA_EXAME = float(input())
    print(f'Nota do exame: {NOTA_EXAME:.1f}')
    MEDIA = (MEDIA + NOTA_EXAME)/2
    if MEDIA >= 5:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print(f'Media final: {MEDIA:.1f}')
elif MEDIA < 50:
    print('Aluno reprovado.')
else:
    print('Aluno aprovado.')