lst = [list(map(int, input().split())) for _ in range(4)]
sum = 0
for i in range(4):
    for j in range(i+1):
        sum += lst[i][j]

print(sum)
