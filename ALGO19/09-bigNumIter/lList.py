class node:
    def __init__(self,val):
        self.data=val
        self.next=None

    def __str__(self):
        if self.next is None:
            return str(self.data)
        else:
            return str(self.next)+str(self.data)

    def __int__(self):
        return int(self.data)
        
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
