i = 3
while i >= 1:
    try:
        print("Resource loaded! Update begins")
        a = int(input("Enter the value of a: "))
        b = int(input("Enter the value of b: "))
        c = a/b
        d = b/a
        i = 0
        print("Update success!")
    except Exception as a:
        i-= 1
        print("Update failed: program error: Error is: ", a)
        if i >= 1:
            print("You have {} attempts to unzip the config package" .format(i))
    finally:
        print("unloading resources..!")

print("Exit")


