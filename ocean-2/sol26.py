a = float(input())
b = float(input())

n = float(input())

if n % a == 0 and n % b == 0:
    print('Divisible by both {0} and {1}'.format(a,b))