a, b = map(int, input().split())
sum = 1
for i in range(1, b+1):
    if not i%a:
        sum *= i

print(sum)