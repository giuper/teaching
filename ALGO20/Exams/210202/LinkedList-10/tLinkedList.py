from linkedList import LinkedList

class TLinkedList(LinkedList):
    def __init__(self,t):
        self.t=t
        self.tries=0
        self=super().__init__()

    def remove(self,element):
        if element not in self:
            return
        if element >= self.t:
            self.tries+=1
            super().remove(element)
            self.insertHead(element)
        else:
            super().remove(element)

    def pop(self,index=None):
        x=super().pop(index)
        if x>=self.t:
            self.insertHead(x)
            self.tries+=1
        return x
        
