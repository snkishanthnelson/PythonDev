class myoriginalclass:
    i = str(5)
    txt = str()

    def printer(self):
        i = "5"
        txt = "We are the so-called \"Vikings\" from the north."
        #example for escape string
        print("The value of i is " + self.i)
        print(txt)



nelson = myoriginalclass()
nelson.printer()

thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)
