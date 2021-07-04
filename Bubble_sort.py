import datetime
def report_to_the_transport_minister(bus_numbers_arrived_today):
    total_trip_counts = len(bus_numbers_arrived_today) - 1
    for j in range(total_trip_counts):
        for i in range(total_trip_counts, 0, -1):
            if bus_numbers_arrived_today[i] < bus_numbers_arrived_today[i-1]:
                temp_variable = bus_numbers_arrived_today[i]
                bus_numbers_arrived_today[i] = bus_numbers_arrived_today[i-1]
                bus_numbers_arrived_today[i-1] = temp_variable
    return bus_numbers_arrived_today

#------------- begin of Main program --------------
# Requirement:
# Create a report to the transport minister from the Bus station log entry.
# Use bubble sort to sort the bus numbers in ascending order
# so the minister will approve the bus entries upon receiving the report.
# The program will be executed everyday by the Station Manager.
# He/She will update the bus_numbers_arrived_today field upon arrival of each bus and execute the program at End of day.
# The output will be directly sent to the minister for approval.
# Duplicate entries should be accepted as few buses with the same number run multiple trips

bus_numbers_arrived_today = [526,232,6,32,67,3424,76,43,77,23,77,90,23,52,34,233,76,232,6,33,22,54,38]
line_breaker ="---------------------------------------------------------------"
print(line_breaker)
print("Galway Bus station - Bus entry approval report for", str(datetime.date.today()))
print(line_breaker)
print("Repected Minister,\nThe bus number(s) arrived today are:")
final_list_to_the_minister = report_to_the_transport_minister(bus_numbers_arrived_today)
print(final_list_to_the_minister)
print("Kindly approve the consolidated payment requests for the transport companies and driver commissions.")
print("Regards, \nStation Manager,\nGalway Bus Station, Galway City.")
print(line_breaker)