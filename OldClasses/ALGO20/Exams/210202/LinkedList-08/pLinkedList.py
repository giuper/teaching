from linkedList import LinkedList

class PLinkedList(LinkedList):
    def __init__(self):
        self.pari=0
        self=super().__init__()

    def insert(self,index,element):
        self.pari=self.pari+1-element%2
        super().insert(index,element)
        
    def insertHead(self,element):
        self.pari=self.pari+1-element%2
        super().insertHead(element)

    def remove(self,target):
        if target in self:
            self.pari=self.pari-(1-target%2)
            super().remove(target)
            
    def pop(self,index=None):
        x=super().pop(index)
        self.pari=self.pari-(1-x%2)
        return x
        
        
