import sys
sys.setrecursionlimit(2000)

i = 0

def greet():
    global i
    i = i + 1
    if i == 1000:
        return()
    print("Hello ", i)
    greet()

greet()