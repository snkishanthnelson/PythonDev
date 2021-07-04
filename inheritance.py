class tamilnadu:
    people = "Bad"
    properties = ['spit','pee in public','nasty fellows']

    def displayproperties(self):
        print("The properties of people are", self.properties)

class salem(tamilnadu):
    population = "1000"

    def whoissalem(self):
        print("Population of salem is {} and people are {}".format(self.population, self.people))

nelson = salem()
nelson.displayproperties()
nelson.whoissalem()
