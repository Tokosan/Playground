import sys

numero = int(sys.argv[1])
cant = int(sys.argv[2])


import math


x = int(math.sqrt(numero))

for i in range(cant):
    x = 0.5 * (x + numero/x)

print(x)

