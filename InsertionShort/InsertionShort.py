b = [5,2,4,6,8,3,5,3,5,7,9,2,2]
def my_function(a):
    for j in range(1, len(a)): #iterate through second to last elements
        key = a[j] #select each time an increasing pivot element
        i = j-1 #index to first left element
        while i >= 0 and a[i] > key: # while higher elements exist more left at the left portion of pivot untill start
            a[i+1] = a[i] #place the greater one position right
            i = i-1 # index to next items as we go left
        a[i+1] = key #place the first key at the correct position
    print(a)
my_function(b)