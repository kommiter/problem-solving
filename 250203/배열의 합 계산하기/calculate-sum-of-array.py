index = [1, 3, 4]
list = [3, 1, 4, 5, 9]
sum = 0
for i in index:
    if i > len(list)-1: continue
    sum += list[i]

print(sum)