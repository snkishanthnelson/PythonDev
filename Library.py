class church:
    def __init__(self, listofmembers):
        self.availablemembers = listofmembers

    def newzoomteammem(self):
        print("Enter a new member")
        availablemembers = listofmembers.input()

    def displayzoomteammem(self):
        for x in availablemembers:
            print(x)

stnicholas = church(['Cathrine', 'Jenefa', 'Lynda', 'Mark', 'Rachel', 'Nelson', 'Mildred'])
stnicholas.mewzoomteammem("Bloomberg")
stnicholas.displayzoomteammem()
