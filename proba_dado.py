from random import randint
import matplotlib.pyplot as pt

N = 100 # cantidad de intentos
n = 6 # cantidad de dados

numeros = [i for i in range(1,7)]

def oks(N,n):
    ok = 0
    for i in range(N):
        num_obt = []
        cumple = True
        for j in range(n):
            cara = randint(1,6)
            num_obt.append(cara)
        for numero in numeros:
            cumple = cumple and numero in num_obt # cumple == True ssi estan todos (1,...,6)
        if cumple:
            ok += 1
    return ok/N

X = [i for i in range(0,30)]
Y = [oks(500,n) for n in range(0,30)]

pt.plot(X,Y)
pt.show()