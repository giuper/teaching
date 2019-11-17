class _DoubleIterator:

    def __init__(self,AAobj):
        self.x=iter(AAobj.x1)
        self.y=iter(AAobj.x2)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            yy=next(self.y)
        except StopIteration:
            yy=None

        try:
            xx=next(self.x)
        except StopIteration:
            xx=None

        if (xx is None) and (yy is None):
            raise StopIteration
        
        if (xx is None):
            return [0,yy]

        if (yy is None):
            return [xx,0]

        return [xx,yy]


class DoubleIter:
    def __init__(self,x,y):
        self.x1=x
        self.x2=y

    def __iter__(self):
        return _DoubleIterator(self)

