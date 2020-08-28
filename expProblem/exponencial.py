#!/usr/local/bin python3
from functools import reduce
from operator import mul

x = int(input("valor de x: "))
n = int(input("valor de n: "))
lista = []
result = 0
res = 0
el = 0
while (n > 1):
    if n % 2 !=0:
        n = n - 1
        lista.append(x)
        el +=1
    else:
        x = x * x
        n = n/2

res = reduce(mul, lista, 1)
print(res)
print (el)

if res == 0:
    print("valor de x e:", x)
else:
    x = res * x
    print("valor de x e:", x)
