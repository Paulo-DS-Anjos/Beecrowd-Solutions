# -*- coding: utf-8 -*-
import math
x1,y1 = map(float,input().split())
x2,y2 = map(float,input().split())
print(f'{(math.sqrt((x2-x1)**2 + (y2-y1)**2)):.4f}')