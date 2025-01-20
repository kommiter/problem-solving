cnt3 = 0
cnt5 = 0
for i in range(10):
    num = int(input())
    if not num%3: cnt3 += 1
    if not num%5: cnt5 += 1

print(cnt3, cnt5, sep = " ")
