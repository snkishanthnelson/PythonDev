def topten():
    i = 1
    while i <= 10:
        square = i*i
        yield square
        i += 1

values = topten()
values2 = list(values)

print(values2)