import math

length = [i for i in range(1, 11)]
value = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]


def barcut(p, n):
    if n == 0:
        return 0
    q = -math.inf
    for i in range(0, n):
        q = max(q, p[i]+ barcut(p, n-i-1))
    return q

print(barcut(value, 9))
