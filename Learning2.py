def count(lst):
    even = 0
    odd = 0
    for i in lst:
        if i%2 == 0:
            even+=1
        else:
            odd+=1

    return(odd,even)


lst = [21,34,55,76,12,88,11,77,65,89]
odd, even = count(lst)
print(odd)
print(even)