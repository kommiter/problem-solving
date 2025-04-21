a, b = map(int, input().split())
sum = 1
for i in range(b):
    sum *= a
print(sum)