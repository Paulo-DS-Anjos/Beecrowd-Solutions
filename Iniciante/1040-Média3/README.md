# 1040 - Média 3

## [Descrição](https://www.urionlinejudge.com.br/judge/pt/problems/view/1040)

Leia quatro números `(N1, N2, N3, N4)`, cada um deles com uma casa decimal, correspondente às quatro notas de um aluno. Calcule a `média com pesos 2, 3, 4 e 1`, respectivamente, para cada uma destas notas e mostre esta média acompanhada pela mensagem `"Media: "`. Se esta média for maior ou igual a 7.0, imprima a mensagem `"Aluno aprovado."`. Se a média calculada for inferior a 5.0, imprima a mensagem `"Aluno reprovado."`. Se a média calculada for um valor entre 5.0 e 6.9, inclusive estas, o programa deve imprimir a mensagem `"Aluno em exame."`.

No caso do aluno estar em exame, leia um valor correspondente à nota do exame obtida pelo aluno. Imprima então a mensagem `"Nota do exame: "` acompanhada pela nota digitada. Recalcule a média (some a pontuação do exame com a média anteriormente calculada e divida por 2). e imprima a mensagem `"Aluno aprovado."` (caso a média final seja 5.0 ou mais ) ou `"Aluno reprovado."`, (caso a média tenha ficado 4.9 ou menos). Para estes dois casos (aprovado ou reprovado após ter pego exame) apresente na última linha uma mensagem `"Media final: "` seguido da média final para esse aluno.

### Entrada:
A entrada contém quatro números de ponto flutuante correspendentes as notas dos alunos.

### Saída:
Todas as respostas devem ser apresentadas com uma casa decimal. As mensagens devem ser impressas conforme a descrição do problema. Não esqueça de imprimir o enter após o final de cada linha, caso contrário obterá "Presentation Error".

## Solução

O mais importante daqui desse exercício é fazer uma parte de cada vez.

1. Calcular a média e exibi-la na tela, respeitando os pesos de cada prova;
2. Ver se o aluno passou, reprovou ou está em exame, exibindo essa informação na tela;
3. Só ler a próxima nota se o aluno estiver em exame e, se for o caso, exibir essa nota nova também;
4. Ver se o aluno passou ou não com a nova média;
5. Independente do aluno passar ou não, exibir a nova média.

Vamos então esquematizar cada um desses passos no nosso programa.

## Python 3.9

```Python
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
elif MEDIA < 5:
    print('Aluno reprovado.')
else:
    print('Aluno aprovado.')
```
