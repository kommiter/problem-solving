a, b = map(int, input().split())
if b < a:
    c = a
    a = b
    b = c
for i in range(b, a-1, -1):
    print(i, end = " ")