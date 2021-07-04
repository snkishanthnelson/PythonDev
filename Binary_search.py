def binary_search(list1, product_number):
    Lower_limit = 0
    Upper_limit = len(list1)
    counter = 0
    for i in range(Lower_limit, Upper_limit):
        mid = int((Lower_limit + Upper_limit) / 2)
        if list1[mid] == product_number:
            counter+=1
            return True, counter
        else:
            counter += 1
            if product_number > list1[mid]:
   #             print("Storage Location routing to: ", list1[mid])
                Lower_limit = mid
            else:
                Upper_limit = mid
   #             print("Storage Location routing to: ", list1[mid])

    return False, counter


#------------- begin of Main program --------------

list1 = []

for i in range(2,502,2):
    list1.append(i)

product_number = int(input("Enter the product serial number:"))

product_result, block_number = binary_search(list1, product_number)

if product_result == True:
    print("GREAT NEWS! The product you are looking for is available at the store! Contact Store helpdesk for collection!")
    print("Store helpdesk - Storage id: {}".format(block_number))
else:
    print("APOLOGIES! The product code is not available. Please call +353-000-10000")
    print("Total searched storage boxes: {}".format(block_number))
print("Thank you! Bye!")



