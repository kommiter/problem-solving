a, b = map(int, input().split())
sum = 0
for i in range(a, b+1):
    if not i%2: sum += i
print(sum)