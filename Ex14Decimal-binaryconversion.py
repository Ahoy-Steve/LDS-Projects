def decbinconv(n):
    if n == 0:
        return ''
    elif n % 2 == 0:
        return '0' + decbinconv(n // 2)
    elif n % 2 == 1:
        return '1' + decbinconv(n // 2)
print(decbinconv(3))