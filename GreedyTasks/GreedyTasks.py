start = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
finish = [4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16]

def greedytasks(s, f):
    f.sort  # finish sorted asceding
    n = len(s)
    iterator = 0
    a = ["a{}".format(iterator)]  # by default add first task  to solution
    k = 0
    for m in range(1, n):  # for k+1 untill final task
        if s[m] >= f[k]:  # find which task m starts right after task k
            a.append("a{}".format(m))  # tasks k and m are conventional, add task m to solution
            k = m  # we look for tasks after task m finishes
    print(a)


greedytasks(start, finish)
