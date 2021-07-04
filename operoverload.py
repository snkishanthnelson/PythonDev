class citilink:
    def __init__(self,sitting,standing):
        self.sitting = sitting
        self.standing = standing

    def __add__(self, other):
        total_sitting = self.sitting + other.sitting
        total_standing = self.standing + other.standing

        return(total_sitting + total_standing)

bus1 = citilink(50,20)
bus2 = citilink(60,45)
print(bus1 + bus2)