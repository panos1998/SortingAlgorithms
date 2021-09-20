import math



def merge(a, start, center, finish):
    L = [0]*(center-start+2)
    R = [0]*(finish-center+1)
    for i in range(0, center-start+1):
        L[i]=a[start+i]
    for j in range(0, finish-center):
        R[j] = a[center+j+1]
    L[center-start+1] = math.inf
    R[finish-center] = math.inf
    print(L)
    print(R)
    i = 0
    j = 0
    for k in range(start, finish+1):
        if L[i] <= R[j]:
            a[k] = L[i]
            i = i+1
        else:
            a[k] = R[j]
            j = j + 1
        k = k + 1
    print(a)




