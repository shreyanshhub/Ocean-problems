s = input()

if s[-1] == 'C':
    print(1.8*int(s[:-1])+32)
else:
    print(0.56*(int(s[:-1])-32))