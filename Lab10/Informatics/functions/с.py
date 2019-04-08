def xor(a, b):
    return (a^b)


s = input().split(' ')
a, b = int(s[0]), int(s[1])
print(xor(a, b))
