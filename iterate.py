class topten:
    def __iter__(self):
        self.init = 2
        return self

    def __next__(self):
        if self.init <= 20:
            val = self.init
            self.init += 2
            return val
        else:
            raise StopIteration



values = topten()
for i in values:
    print(i)
