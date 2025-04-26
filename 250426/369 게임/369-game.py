n = int(input())
for i in range(1, n + 1):
    if not i % 3 or any(d in str(i) for d in '369'): print(0, end=' ')
    else: print(i, end=' ')