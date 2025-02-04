start, end = map(int, input().split())

# Please write your code here.
rt = 0
for i in range(start, end+1):
    sum = 0
    for j in range(1, i+1):
        if not i % j: sum += 1
    if sum is 3: rt += 1
print(rt)