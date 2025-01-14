n = int(input())
lst = list(map(int, input().split()))
lst.reverse()
print(*[x for x in lst if not x % 2])