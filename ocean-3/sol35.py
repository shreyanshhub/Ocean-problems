def fib(n):
    l = [i for i in range(n)]
    l[0],l[1] = 1,1
    for i in range(2,n):
        l[i] = l[i-1] + l[i-2]
    return l[n-1]