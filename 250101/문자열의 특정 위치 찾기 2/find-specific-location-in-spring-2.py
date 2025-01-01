c = input()
sum = 0
lst = ["apple", "banana", "grape", "blueberry", "orange"]
for i in lst:
    if c is i[2] or c is i[3]:
        print(i)
        sum += 1

print(sum)