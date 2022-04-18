from random import randint

A = [3,3,3,3,3,6]
B = [4,4,4,4,4,1]
C = [2,2,2,5,5,5]

# 1. Maria escoje A. Esto viene de Juan escogiendo C o B

resultado = 0 # guarda 0 si pierde, 1 si gana
resultados = 0 # guarda 0 si pierde, 1 si gana
n = 100 # cantidad de intentos
N = 10000

J = [C]
M = B

for k in range(N):
    
    resultado = 0
    
    for i in range(n):

        j = randint(0,5)
        m = randint(0,5)
        Juan = J[randint(0,len(J)-1)][j]
        Maria = M[m]

        if Maria>Juan:
            resultado += 1

    resultados += resultado/n
print(f'{resultado}/{n}')   
print(f'{int(resultados)}/{N}')
print(round(resultados/N,2))
