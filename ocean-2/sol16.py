vowels = 'aeiou'

d = {'vowels':0,'consonants':0}

s = input()

def count(s,d):
    for i in s:
        if s in vowels:
            d['vowels'] += 1
        else:
            d['consonants'] += 1
    return d 

print(count(s,d))