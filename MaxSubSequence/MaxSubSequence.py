import math
from MaxOnBothSides import maxonbothsides


def maxsubsequence(array, down, up):
    if down == up:
        return down, up, array[down]
    else:
        center = math.floor((down+up)/2)
        left_down, left_up, left_sum = maxsubsequence(array, down, center)
        right_down, right_up, right_sum = maxsubsequence(array, center+1, up)
        both_down, both_up, both_sum = maxonbothsides(array, down, center, up)
        if left_sum >= right_sum and left_sum >= both_sum:
            return left_down, left_up, left_sum
        elif right_sum >= left_sum and right_sum >= both_sum:
            return right_down, right_up, right_sum
        else:
            return both_down, both_up, both_sum


A = [-5, -1, 0, 2, 7]
print(maxsubsequence(A, 0, len(A)-1))
