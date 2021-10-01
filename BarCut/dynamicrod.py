import math

length = [i for i in range(1, 11)]
value = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

def dynamicrod(p, n):
    r = [0 for k in range(n+1)]
    r[0] = 0
    for j in range(1, n+1):
        q = -math.inf
        for i in range(j):
            q = max(q, p[i] + r[j-1-i])
        r[j] = q
    return r[n]


x = dynamicrod(value, 10)
print(x)