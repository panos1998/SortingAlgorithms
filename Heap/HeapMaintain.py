import math


def heapmaintain(a, i):
    left = 2*i
    r = 2*i + 1
    if left <= len(a) and a[left] > a[i]:
        max_pos = left
    else:
        max_pos = i
    if r <= len(a) and a[r] > a[max_pos]:
        max_pos = r
    if max_pos != i:
        temp = a[i]
        a[i] = a[max_pos]
        a[max_pos] = temp
        heapmaintain(a, max_pos)
    print(a)

def maxheapconstruct(a):
    n = len(a)
    for i in range (math.floor(n/2)-1, 0, -1):
        heapmaintain(a, i)


array = [16, 4, 10, 14, 7, 9, 3, 2, 9, 1]
maxheapconstruct(array)

def heapsort(a):
    for i in range(len(a)-1, 1, -1):
        temp = a[0]
        a[0] = a[i]
        a[i] = temp
        n = len(a) -1
        heapmaintain(a, 1)


heapsort(array)