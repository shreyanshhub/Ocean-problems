n = int(input())

def dtb(n):
    if n >= 1:
        dtb(n//2)
    print(n%2,end='')