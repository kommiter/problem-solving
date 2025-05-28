flag = False
for i in range(5):
    num = int(input())
    if num%3:
        flag = True
        break

print(0 if flag else 1)