a, b = map(int, input().split())
arr = [a >= b, a > b, b >= a, b > a, a == b, a != b]
for i in arr: print(1 if i else 0)