n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())
n5 = float(input())

avg = sum([n1,n2,n3,n4,n5])/5

if avg >= 90:
    print('A')
elif avg < 90 and avg >= 80:
    print('B')
elif avg >= 70 and avg < 80:
    print('C')
elif avg >= 60 and avg < 70:
    print('D')
else:
    print('F')