import time
import random
Teamdict ={1:'Dublin',2:'Galway',3:'Wexford',4:'Watrerford',5:'Mayo',6:'Cork',7:'Donegal',8:'Limerick'}

Team_fixture_order = []
while len(Team_fixture_order) < 8:
    Lotto_number = round(random.random()*10)
    if Lotto_number < 1 or Lotto_number > 8:
        continue
    if len(Team_fixture_order) == 0:
        Team_fixture_order.append(Lotto_number)
    elif len(Team_fixture_order) < 8:
        for i in range(len(Team_fixture_order)):
            if Lotto_number == Team_fixture_order[i]:
                break
        else:
            Team_fixture_order.append(Lotto_number)

for i in range(0,7,2):
    print(Teamdict[Team_fixture_order[i]], "vs", Teamdict[Team_fixture_order[i+1]])
    time.sleep(0.5)

