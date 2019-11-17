from lList import lList
from doubleIter import DoubleIter

class _bigNumIterator:
    def __init__(self,bn):
        self.iter=iter(bn.list)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.iter)

class bigNum:
##construct a bigNum from its string representation
##digits of a bigNum appear from least to most significant
    def __init__(self,val=""):
        self.list=lList()
        for x in val:
            self.list.insert(x)
        
    def __iter__(self):
        return _bigNumIterator(self)

    def insertDigit(self,val):
        self.list.insert(val)
        
    def appendDigit(self,val):
        self.list.append(val)

    def __add__(self,other):
        result=bigNum()
        carry=0
        zz=DoubleIter(self,other)
        for n in zz:
            dgt=int(n[0])+int(n[1])+carry
            result.appendDigit(str(dgt%10))
            carry=dgt//10

        if (carry!=0):
            result.appendDigit(str(carry))

        return(result)
            
        
    def multbyadigit(self,valInt):
        carry=0
        result=bigNum()
        for a in self:
            dgt=carry+int(a)*valInt
            result.appendDigit(str(dgt%10))
            carry=dgt//10

        while(carry!=0):
            result.appendDigit(str(carry%10))
            carry=carry//10
        
        return result
        
    def _multbyten(self,t):
        for i in range(t):
            self.insertDigit("0")

    def __mul__(self,other):
        result=bigNum()
        t=0
        for a in other:
            temp=self.multbyadigit(int(a))
            temp._multbyten(t)
            result=result+temp
            t=t+1

        return result

    def __str__(self):
        return str(self.list)
             
