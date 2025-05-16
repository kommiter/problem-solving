while True:
    line = input().strip()
    width, height, c = line.split()
    
    area = int(width) * int(height)
    print(area)

    if c == 'C':
        break