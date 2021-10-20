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

class _lListIterator:
    def __init__(self,l):
        self.curNode=l.head

    def __iter__(self):
        return self

    def __next__(self):
        if self.curNode is not None:
            item=self.curNode.data
            self.curNode=self.curNode.next
            return item
        else:
            raise StopIteration
        
class lList:
    def __init__(self):
        self.head=None
        self.tail=None

    def __iter__(self):
        return _lListIterator(self)

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
