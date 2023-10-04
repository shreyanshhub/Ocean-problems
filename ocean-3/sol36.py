from random import randint 

def throw_simulation(n):

    bins = [0 for i in range(n)]

    for i in range(1,n):

        r = randint(0,n-1)
        bins[r] += 1 

    maximum = max(bins)
    return maximum

k = 10
l = [throw_simulation(10) for i in range(k)] #n=10
avg1 = sum(l)/k
print(avg1)

k = 100 
l = [throw_simulation(10) for i in range(k)] #n=10
avg2 = sum(l)/k
print(avg2)

k = 1000
l = [throw_simulation(100) for i in range(k)] #n=100
avg3 = sum(l)/k
print(avg3)

k = 10000
l = [throw_simulation(100) for i in range(k)] #n=100
avg4 = sum(l)/k
print(avg4)
