a = int(input())
for i in range(1, a+1):
    flag1 = not i%2 and i%4
    flag2 = not (i//8)%2
    flag3 = i%7 < 4
    if not flag1 and not flag2 and not flag3:
        print(i, end = " ")