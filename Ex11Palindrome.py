def palindrome(n):
    if len(n)<=1:
        return True
    if n[0] != n[-1]:
        return False
    else:
        return palindrome(n[1:-1])
print(palindrome("222"))