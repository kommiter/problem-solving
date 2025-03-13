sum = 0
cnt = 0
for i in range(10):
    num = int(input())
    if num < 0 or num > 200: continue
    sum += num
    cnt += 1

print(f"{sum} {sum/cnt:.1f}")