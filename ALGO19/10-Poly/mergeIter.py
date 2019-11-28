class _MergeIterator:

    def __init__(self,AAobj):
        self.x=iter(AAobj.x1)
        self.y=iter(AAobj.x2)
        self.cachex=None
        self.cachey=None

    def __iter__(self):
        return self

    def __next__(self):
        if self.cachey is None:
            try:
                yy=next(self.y)
            except StopIteration:
                yy=None
        else:
            yy=self.cachey

        if self.cachex is None:
            try:
                xx=next(self.x)
            except StopIteration:
                xx=None
        else:
            xx=self.cachex

        if (xx is None) and (yy is None):
            raise StopIteration
        
        if (xx is None):
            self.cachey=None
            return yy

        if (yy is None):
            self.cachex=None
            return xx

        if (xx==yy):
            self.cachex=None
            self.cachey=None
            return xx+yy

        if (xx<yy):
            self.cachex=None
            self.cachey=yy
            return xx
        else:
            self.cachey=None
            self.cachex=xx
            return yy


class MergeIter:
    def __init__(self,x,y):
        self.x1=x
        self.x2=y

    def __iter__(self):
        return _MergeIterator(self)

