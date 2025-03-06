n = int(input())
cnt = 0
for i in range(1, n+1):
    leap_flag = not i%4
    common_flag = not i%100 and i%400
    if leap_flag and not common_flag: cnt += 1
    
print(cnt)