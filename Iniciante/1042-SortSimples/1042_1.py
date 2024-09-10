V = list(map(int,input().split()))
v = V[:]
v.sort()

for i in range(3):
    print(v[i])
print()
for i in range(3):
    print(V[i])