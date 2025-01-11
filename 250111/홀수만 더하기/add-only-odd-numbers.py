n = int(input())
sum = 0
for i in range(n):
    num = int(input())
    if not num%3 and num%2: sum += num

print(sum)