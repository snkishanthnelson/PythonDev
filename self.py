class Man:
    def __init__(self, name1, name2):
        self.name = name1
        self.name2 = name2

    def displaydetails(self):
        print(self.name)
        print(self.name2)

nelson = Man("Nelson","sigamoney")
Jenefa = Man("Jenefa","Merlyn")
nelson.displaydetails()
Jenefa.displaydetails()
