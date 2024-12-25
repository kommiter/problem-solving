n = int(input())
for i in range(1, n+1):
    for j in range(1, n+1):
        print(f"{i} * {j} = {i*j}", end = "")
        if j is not n: print(", ", end = "")
    print()