n = int(input())
cur = 1
for i in range(1, n+1):
    for j in range(i):
        print(cur, end = " ")
        cur += 1
    print()