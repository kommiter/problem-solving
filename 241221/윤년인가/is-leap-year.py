y = int(input())
leap_flag = not y%4
common_flag = not y%100 and y%400

print("true" if leap_flag and not common_flag else "false")