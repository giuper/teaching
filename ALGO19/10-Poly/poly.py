from lList import lList
from mergeIter import MergeIter

class Monomial:

    def __init__(self,c,e):
        self.c=c
        self.e=e

    def __mul__(self,other):
        return Monomial(self.c*other.c,self.e+other.e)

    def __add__(self,other):
        return Monomial(self.c+other.c,self.e)

    def __eq__(self,other):
        return self.e==other.e

    def __gt__(self,other):
        return self.e>other.e

    def __lt__(self,other):
        return self.e<other.e

    def __str__(self):
        if self.c==1  and self.e==0:
                return("+1")
        if self.c==-1 and self.e==0:
                return("-1")

        if self.c==1  and self.e==1:
                return("+x")
        if self.c==-1 and self.e==1:
                return("-x")

        if self.c==1 and self.e>1:
            return("+x^"+str(self.e))

        if self.c==-1 and self.e>1:
            return("+x^"+str(self.e))
        
        if self.c>0:
            return("+"+str(self.c)+"*x^"+str(self.e))
        else:
            return("-"+str(-self.c)+"*x^"+str(self.e))



class _PolyIterator:
    def __init__(self,p):
        self.iter=iter(p.list)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.iter)


class Polynomial:

        def __init__(self):
            self.list=lList()

        def __iter__(self):
            return _PolyIterator(self)

        def append(self,mono):
            self.list.append(mono)

        def insert(self,mono):
            self.list.insert(mono)

        def __str__(self):
            return str(self.list)[1:]
        
        def __add__(self,other):
            zz=MergeIter(self,other)
            res=Polynomial()
            for m in zz:
                if (m.c!=0):
                    res.append(m)
            return res

        def __add1__(self,other):
            a=self.list.head
            b=other.list.head
            res=Polynomial()
            while a is not None and b is not None:
                if a.data.e==b.data.e:
                    newc=a.data.c+b.data.c
                    if newc!=0:
                        res.append(Monomial(newc,a.data.e))
                    a=a.next
                    b=b.next
                    continue
                
                if a.data.e<b.data.e:
                    res.append(Monomial(a.data.c,a.data.e))
                    a=a.next
                else:
                    res.append(Monomial(b.data.c,b.data.e))
                    b=b.next
                    
            while a is not None:
                res.append(Monomial(a.data.c,a.data.e))
                a=a.next 
             
            while b is not None:
                res.append(Monomial(b.data.c,b.data.e))
                b=b.next
            return res

        def mulByMono(self,m):
            res=Polynomial()

            for n in self:
                rm=n*m
                res.append(rm)
                
            return res

        def __mul__(self,other):
            res=Polynomial()
            for ms in other:
                temp=self.mulByMono(ms)
                res=res+temp
            return res
