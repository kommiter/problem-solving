a, b = map(int, input().split())

i = a
while True:
    if i > b: break
    print(i, end = " ")
    if i%2: i *= 2
    else: i += 3