def power(a, n):
    return a ** n


s = input().split(' ')

a, b = float(s[0]), int(s[1])

print(power(a, b))
