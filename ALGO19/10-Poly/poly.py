from lList import lList

class Monomial:

    def __init__(self,c,e):
        self.c=c
        self.e=e

    def __mul__(self,other):
        return Monomial(self.c*other.c,self.e+other.e)

    def __str__(self):
        return(str(self.c)+"*x^"+str(self.e))+"+"


class Polynomial:

        def __init__(self):
            self.list=lList()

        def append(self,mono):
            self.list.append(mono)

        def insert(self,mono):
            self.list.insert(mono)

        def __str__(self):
            return str(self.list)[:-1]
        
        def __add__(self,other):
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

            for n in self.list:
                rm=n*m
                res.append(rm)
                
            return res

            
