from random import randint 

def throw_balls(n):

    bins = [0]*n
    d = {}

    while True:

        if 0 not in bins:
            break 
        
        i = randint(0,n-1)

        bins[i] += 1 

    return max(bins)

