from linkedList import LinkedList

class bigNum:
##construct a bigNum from its string representation
##digits of a bigNum appear from least to most significant
    def __init__(self,val=""):
        self.list=LinkedList()
        for x in val:
            self.list.insertHead(x)
        
    def __add__(self,other):
        result=bigNum()
        a=self.list.head
        b=other.list.head
        carry=0
        while (a is not None) and (b is not None):
            dgt=int(a.data)+int(b.data)+carry
            result.list.append(str(dgt%10))
            carry=dgt//10
            a=a.next
            b=b.next

        while(a is not None):
            dgt=carry+int(a.data)
            result.list.append(str(dgt%10))
            carry=dgt//10
            a=a.next

        while(b is not None):
            dgt=carry+int(b.data)
            result.list.append(str(dgt%10))
            carry=dgt//10
            b=b.next

        if (carry!=0):
            result.list.append(str(carry))

        return(result)
            
#def __mul__(self,other):

    def __str__(self):
        res=""
        for a in self.list:
            res=str(a)+res
        return res
             
