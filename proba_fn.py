import matplotlib.pyplot as pt

def f(n):
    return 1 - 6*(5/6)**n + 15*(4/6)**n - 20*(3/6)**n + 15*(2/6)**n - 6*(1/6)**n

N = [i for i in range(6,30)]
F = [f(i) for i in range(6,30)]

pt.plot(N,F)
pt.show()

print(f(6))