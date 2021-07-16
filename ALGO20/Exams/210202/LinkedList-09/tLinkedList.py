from linkedList import LinkedList

class TLinkedList(LinkedList):
    def __init__(self,t):
        self.t=t
        self.tries=0
        self=super().__init__()

    def insert(self,index,element):
        if element >= self.t:
            self.tries+=1
        else:
            super().insert(index,element)
        
    def insertHead(self,element):
        if element >= self.t:
            self.tries+=1
        else:
            super().insertHead(element)

        
