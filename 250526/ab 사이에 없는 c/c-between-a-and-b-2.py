a, b, c = map(int, input().split())
flag = False
for i in range(a, b+1):
    if not i%c:
        flag = True
        break

print("NO" if flag else "YES")
