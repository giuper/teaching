from lList import lList

class _bigNumIterator:
    def __init__(self,node):
        self.curNode=node

    def __iter__(self):
        return self

    def __next__(self):
        if self.curNode is not None:
            item=self.curNode
            self.curNode=self.curNode.next
            return item
        else:
            self.curNode=None
            raise StopIteration

class _bigNumDoubleIterator:
    def __init__(self,x,y):
        self.zx=x.__iter__()
        self.zy=y.__iter__()

    def getNext(self):
        try: 
            nx=self.zx.__next__()
        except StopIteration:
            nx=None;

        try: 
            ny=self.zy.__next__()
        except StopIteration:
            ny=None;

        if (nx is None) and (ny is None):
            return None

        if (nx is None):
            return ["0",ny]

        if (ny is None):
            return [nx,"0"]

        return [nx,ny]
        

class bigNum:
##construct a bigNum from its string representation
##digits of a bigNum appear from least to most significant
    def __init__(self,val=""):
        self.list=lList()
        for x in val:
            self.list.insert(x)
        
    def __iter__(self):
        return _bigNumIterator(self.list.head)

    def insertDigit(self,val):
        self.list.insert(val)
        
    def appendDigit(self,val):
        self.list.append(val)
        

    def __add__(self,other):
        result=bigNum()
        zz=_bigNumDoubleIterator(self,other)
        carry=0
        n=zz.getNext()
        while n is not None:
            dgt=int(n[0])+int(n[1])+carry
            result.appendDigit(str(dgt%10))
            carry=dgt//10
            n=zz.getNext()

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
             
