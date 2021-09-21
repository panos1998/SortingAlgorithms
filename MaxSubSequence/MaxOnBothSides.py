import math as math


def maxonbothsides(array, down, center, up):
                                          # A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
     sum_left = -math.inf  # best score  untill each iteration
     Sum = 0               # current score
     for i in range(center, down-1, -1):
         Sum = Sum + array[i] # calculate score for each iteration
         if Sum > sum_left:   # if current score is better than best  untill now score
             sum_left = Sum  # update best score
             max_left = i    # at which position ends  the best score sum?
     sum_right = -math.inf
     Sum = 0
     for j in range(center+1, up+1):
         Sum = Sum + array[j]
         if Sum > sum_right:
             sum_right = Sum
             max_right = j

     return (max_left, max_right, sum_left + sum_right )

