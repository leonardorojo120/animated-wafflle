def calc(*args):
    sum = 0
    for item in args:
        sum += item
    return sum

t = calc(2,2,5)
print(t)