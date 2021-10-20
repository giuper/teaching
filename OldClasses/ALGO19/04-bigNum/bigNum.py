class node:
    def __init__(self,val):
        self.data=val
        self.next=None

    def __str__(self):
        if self.next is None:
            return str(self.data)
        else:
            return str(self.next)+str(self.data)
        
class lList:
    def __init__(self):
        self.head=None
        self.tail=None

    def append(self,val):
        n=node(val)
        if self.head==None:
            self.head=n
            self.tail=n
        else:
            self.tail.next=n
            self.tail=n
            
    def insert(self,val):
        n=node(val)
        if self.head==None:
            self.head=n
            self.tail=n
        else:
            n.next=self.head
            self.head=n
        
    def __str__(self):
        if self.head is None:
            return ""
        else:
            return str(self.head)


class bigNum:
##construct a bigNum from its string representation
##digits of a bigNum appear from least to most significant
    def __init__(self,val=""):
        self.list=lList()
        for x in val:
            self.list.insert(x)
        
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
        return str(self.list)
             
