n = int(input())
for i in range(n):
    if i%2:
        for j in range(n, 0, -1):
            print(j, end = "")
        print()

    else:
        for j in range(n):
            print(j+1, end = "")
        print()