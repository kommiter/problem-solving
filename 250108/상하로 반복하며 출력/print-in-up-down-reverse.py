n = int(input())
for i in range(n):
    for j in range(n):
        print(n-i if j%2 else i+1, end = "")
    print()