n = int(input())
for i in range(1, n+1):
    flag1 = not i%2
    flag2 = not i%3
    if flag1 or flag2: print(1, end = " ")
    else: print(0, end = " ")