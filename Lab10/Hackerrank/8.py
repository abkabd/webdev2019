n = int(input())
arr = list(map(int, input().split()))
arr.sort()
while arr[n-1] == arr[n-2]:
    n -= 1
else:
    print(arr[n-2])
