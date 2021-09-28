array = [2, 8, 7, 1, 3, 5, 6]


def partition(a, p, r):
    x = a[r]
    i = p - 1
    for j in range(p, r):
        if a[j] <= x:
            i = i+1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[r] = a[r], a[i+1]
    return i + 1


def quicksort(a, p, r):
    if p == r:
        return a
    elif p < r:
        q = partition(a, p, r)
        quicksort(a, p, q-1)
        quicksort(a, q + 1, r)


quicksort(array, 0, 6)
print(array)

