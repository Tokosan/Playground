from math import factorial as f

def sobre(n,k):
    return f(n) / (f(n-k) * f(k))

def F(n):
    return 1/6 * sum([
        sobre(k,n)*(2**(-k))
        for k in range(n,6+1)
    ])

F0 = 1/6 * sum([2**(-k) for k in range(1,6+1)])

print(0*F0 + sum([k*F(k) for k in range(1,6+1)]))