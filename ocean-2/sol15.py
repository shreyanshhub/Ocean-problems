n = input()

def palindrome(n):
    return n == n[::-1]

print(palindrome(n))