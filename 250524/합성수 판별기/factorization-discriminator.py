n = int(input())
flag = False
for i in range(2, n):
    if not n%i:
        flag = True
        break

print("N" if not flag else "C")