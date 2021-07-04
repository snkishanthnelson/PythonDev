#Program to generate fixtures for the first round of the next Hurling Knockout tournament across all Irish counties.
#This will be broadcasted via RTE. So ensure there is 0.5 sec gap while printing each game fixture.
import time
import random
Teamdict ={1:'Dublin',2:'Galway',3:'Wexford',4:'Watrerford',5:'Mayo',6:'Cork',7:'Donegal',8:'Limerick',9:'Tipperary',
           10:'Cavan',11:'Leitrim',12:'Monaghan',13:'Sligo',14:'Kildare',15:'Louth',16:'Meath',17:'Wicklow',
           18:'Clare',19:'Laois',20:'Longford',21:'Offaly',22:'Carlow',23:'Kilkenny',24:'Westmeath',25:'Kerry',
           26:'Roscommon'}

Team_fixture_order = []
while len(Team_fixture_order) < 26:
    Lotto_number = round(random.random()*100)
    if Lotto_number < 1 or Lotto_number > 26:
        continue
    if len(Team_fixture_order) == 0:
        Team_fixture_order.append(Lotto_number)
    elif len(Team_fixture_order) < 26:
        for i in range(len(Team_fixture_order)):
            if Lotto_number == Team_fixture_order[i]:
                break
        else:
            Team_fixture_order.append(Lotto_number)

j = 0
for i in range(0,25,2):
    j+=1
    print(j, Teamdict[Team_fixture_order[i]], "vs", Teamdict[Team_fixture_order[i+1]])
    time.sleep(0.5)

