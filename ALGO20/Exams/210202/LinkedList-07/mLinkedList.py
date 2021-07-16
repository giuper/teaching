from linkedList import LinkedList

class MLinkedList(LinkedList):
    def __init__(self):
        self.max=float("-inf")
        self=super().__init__()

    def append(self,element):
        if element>self.max:
            self.max=element
        super().append(element)

    def insert(self,index,element):
        if element>self.max:
            self.max=element
        super().insert(index,element)
        
    def insertHead(self,element):
        if element>self.max:
            self.max=element
        super().insertHead(element)
