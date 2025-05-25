a, b = map(int, input().split())

flag = False
for i in range(a, b+1):
    if not 1920%i and not 2880%i:
        flag = True
        break

print("1" if flag else "0")