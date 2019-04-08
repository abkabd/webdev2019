def min2(a, b):
    if a < b:
        return a
    else:
        return b


def min(a, b, c, d):
    return min2(min2(a, b), min2(c, d))


s = input().split(' ')

a, b, c, d, = int(s[0]), int(s[1]), int(s[2]), int(s[3])

print(min(a, b, c, d))
