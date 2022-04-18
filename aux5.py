import numpy as np

def ataque(i,j):
    for k in range(8):
        if tablero[i][k] == 1 or tablero[k][j] == 1: return True
    for k in range(8):
        for l in range(8):
            if tablero[k][l] == 1 and ( k - l  == i - j or k + l == i + j): return True

def reinas(n = 8):
    if n == 0: return True
    for i in range(8):
        for j in range(8):
            if not ataque(i,j):
                tablero[i][j] = 1
                if reinas(n - 1):
                    return True
                tablero[i][j] = 0
        return False

tablero = np.zeros((8,8),int)

print(tablero)

def levenshtein_recursivo(S,T):
    def D(i,j):