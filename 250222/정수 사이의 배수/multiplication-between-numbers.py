a, b = map(int, input().split())
cnt = 0
sum = 0
for i in range(a, b+1):
    if not i%5 or not i%7:
        cnt += 1
        sum += i

print(f"{sum} {sum/cnt:.1f}")