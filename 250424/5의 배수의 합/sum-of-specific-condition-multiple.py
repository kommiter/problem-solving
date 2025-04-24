a, b = map(int, input().split())
sum = 0
if b < a:
    c = a
    a = b
    b = c
for i in range(a, b+1):
    if not i%5: sum += i
print(sum)