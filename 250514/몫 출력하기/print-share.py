while True:
    try:
        n = int(input())
        if not n%2: print(int(n/2))
    except EOFError:
        break