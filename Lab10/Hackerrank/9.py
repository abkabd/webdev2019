a = list()
for _ in range(int(input())):
    s = input().split(' ')
    if s[0] == 'insert':
        a.insert(int(s[1]), int(s[2]))
    if s[0] == 'print':
        print(a)
    if s[0] == 'remove':
        a.remove(int(s[1]))
    if s[0] == 'append':
        a.append(int(s[1]))
    if s[0] == 'sort':
        a.sort()
    if s[0] == 'pop':
        a.pop()
    if s[0] == 'reverse':
        a.reverse()
