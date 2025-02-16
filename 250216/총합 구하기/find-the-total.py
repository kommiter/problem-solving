a, b = map(int, input().split())

sum = 0
for i in range(a, b+1):
    if not i%6 and i%8:
        sum += i

print(sum)