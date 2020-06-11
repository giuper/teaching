class Bag1Iter:

    def __init__(self,theList):
        self.items=theList
        self.cur=None

    def __iter__(self):
        return self

    def __next__(self):
        if self.cur is None: #prima volta restituisco il minimo
            m=self.items[0]
            for i in range(len(self.items)):
                x=self.items[i]
                if x<m:
                    m=x
            self.cur=m
            return m

        m=None
        for i in range(len(self.items)):
            x=self.items[i]
            if x<self.cur:
                continue
            if m is None and x>self.cur:
                m=x
            if m is not None and x>self.cur and x<m:
                m=x

        if m is None:
            raise StopIteration
        else:
            self.cur=m
            return m

class Bag1:

    def __init__(self):
        self.items=list()

    def add(self,x):
        self.items.append(x)

    def __len__(self):
        return len(self.items)

    def __contains__(self,x):
        return x in self.items


    def add1(self,x):
        found=0
        for i in range(len(self.items)):
            if self.items[i]==x:
                found=found+1
        if found<2:
            self.add(x)
            
    def Min(self):
        res=None
        for i in range(len(self.items)):
            y=self.items[i]
            if res is None:
                res=y
            else:
                if res>y:
                    res=y
        return res

    def __iter__(self):
        return Bag1Iter(self.items)

    def timeAdded(self):
        return self.items


