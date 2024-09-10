# -*- coding: utf-8 -*-
p1 , p2 = map(int, input().split())
if p1 == 1:
    print(f'Total: R$ {(p2*4):.2f}')
elif p1 == 2:
    print(f'Total: R$ {(p2*4.5):.2f}')
elif p1 == 3:
    print(f'Total: R$ {(p2*5):.2f}')
elif p1 == 4:
    print(f'Total: R$ {(p2*2):.2f}')
elif p1 == 5:
    print(f'Total: R$ {(p2*1.5):.2f}')