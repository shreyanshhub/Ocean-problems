n = int(input())

def isprime(n):
    if n < 2:
        return False
    for i in range(2,int(pow(n,0.5))):
        if n % i == 0:
            return False

    return True

print(isprime(n))
