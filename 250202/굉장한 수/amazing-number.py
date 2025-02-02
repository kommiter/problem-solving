n = int(input())
flag1 = n%2 and not n%3
flag2 = not n%2 and not n%5
print("true" if flag1 or flag2 else "false")