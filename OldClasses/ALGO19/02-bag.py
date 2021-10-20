class BagIter:

    def __init__(self,theList):
        self.bagItems=theList
        self.cur=0

    def __iter__(self):
        return self

    def __next__(self):
        if self.cur<len(self.bagItems):
            item=self.bagItems[self.cur]
            self.cur+=1
            return item
        else:
            raise StopIteration


class Bag:

    def __init__(self):
        self.items=list()

    def add(self,x):
        self.items.append(x)

    def __len__(self):
        return len(self.items)

    def __contains__(self,x):
        return x in self.items

    def __iter__(self):
        return BagIter(self.items)

B=Bag()
B.add(12)
B.add(21)
B.add(7)
print (len(B))
if 9 in B:
    print ("Trovato")
else:
    print ("Non trovato")

if 7 in B:
    print ("Trovato")
else:
    print ("Non trovato")

for x in B:
    print(x)

