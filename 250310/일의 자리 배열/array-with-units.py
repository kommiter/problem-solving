lst = list(map(int, input().split()))
for i in range(2, 10):
    lst.append((lst[i-2]+lst[i-1])%10)

for i in lst:
    print(i, end = " ")