n = int(input())

for i in range(1, 5001):
    n //= i
    if n <= 1:
        print(i)
        break