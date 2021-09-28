import random

def simplemult(a, b):

 c = [[0 for m in range(len(b))] for h in range(len(a))]
 for i in range(len(a)):
     for j in range(len(b[0])):
         for k in range(len(b)):
             c[i][j] += a[i][k]*b[k][j]
 print (c)


k = [[i*j  for i in range(5)]  for j in range(4)]
x = [[(1+i)*(j+1) for i in range(4)]  for j in range(5)]


simplemult(k, x)
