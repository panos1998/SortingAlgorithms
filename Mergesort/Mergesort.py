import math
from Merge import merge
Array = [5, 6, 3, 2, 6, 3, 6, 9, 4, 3, 2, 1]


def mergesort(a, p, r):
    if p < r:
        q = math.floor((p+r)/2)
        mergesort(a, p, q)
        mergesort(a, q+1, r)
        merge(a, p, q, r)


mergesort(Array, 0, len(Array)-1)
