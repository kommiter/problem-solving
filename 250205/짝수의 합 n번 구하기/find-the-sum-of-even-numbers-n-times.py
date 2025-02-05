n = int(input())
for i in range(n):
    sum = 0
    a, b = map(int, input().split())
    for j in range(a, b+1):
        if not j % 2: sum += j
    print(sum)