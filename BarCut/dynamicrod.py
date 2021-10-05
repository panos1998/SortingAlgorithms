import math

length = [i for i in range(1, 11)]
value = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

def dynamicrod(p, n):
    r = [0 for k in range(n+1)]
    r[0] = 0
    for j in range(1, n+1): # for each bar element
        q = -math.inf
        for i in range(j): # for each bar element from start to  selected element p[j]
            q = max(q, p[i] + r[j-1-i]) # solve the subproblems
        r[j] = q # save best solution for current element p[j] inside r
    return r[n] # return the last element of r == the best solution for last element == the best solution for whole problem


x = dynamicrod(value, len(value))
print(x)