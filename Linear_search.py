def exam_result(List1, n):
    counter_loc = 0
    for i in List1:
        counter_loc += 1
        if n == i:
            return True, counter_loc
    return False, counter_loc


List1 = [2121,34343,6565,23235454,6565,3,1,4,54545,45454,54545,54545,233232,2323,3,32323,3232,22121,7767,68785,44342,32]
print("Welcome to Citlink Luxury Cruise: London to Budapist")
print("---------------------------------------------------------")
print("Vaccination - verification - Ticket confirmation page")
print("---------------------------------------------------------")

i = 3
while i > 0:
    n = int(input("Enter your HSC Vaccination-Ticket match number :"))
    x,y = exam_result(List1,n)
    if x == True:
        print("Your ticket is approved for travel by the embassy! Your entry id is {}" .format(y))
        i = 0
    else:
        if i > 1:
            i = i - 1
            print("No updates! Kindly try again! You have {} more attempts left!" .format(i))
        elif i == 1:
            i = 0
            print("You have exceeded the access limit! Try again after sometime!")
