n = int(input())
cnt2 = 0
cnt3 = 0
cnt12 = 0
for i in range(1, n+1):
    if not i%12: cnt12 += 1
    elif not i%3: cnt3 += 1
    elif not i%2: cnt2 += 1

print(cnt2, cnt3, cnt12, sep = " ")