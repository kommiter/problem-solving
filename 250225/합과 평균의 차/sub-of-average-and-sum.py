a, b, c = map(int, input().split())
sum = a + b + c
avg = sum // 3

print(sum, avg, sum-avg, sep="\n")