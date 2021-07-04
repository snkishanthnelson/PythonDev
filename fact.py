def fact(n):
    factor = 1
    for i in range(n, 1, -1):
        factor = factor * i
    return(factor)


n = int(input("Enter the value of factorial number: "))
result = fact(n)
print(result)
