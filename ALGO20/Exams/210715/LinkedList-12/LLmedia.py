from linkedList import LinkedList

class LLmedia(LinkedList):

    def __init__(self):
        super().__init__()
        self.somma=0

    def media(self):
        if len(self)==0:
            return 0
        else:
            return self.somma/len(self)

    def insert(self,index,elem):
        self.somma=self.somma+elem
        super().insert(index,elem)

    def insertHead(self,elem):
        self.somma=self.somma+elem
        super().insertHead(elem)

    def pop(self,index=None):
        elem=super().pop(index)
        self.somma=self.somma-elem
        return elem

    def remove(self,target):
        initialSize=len(self)
        super().remove(target)
        if len(self)!=initialSize:
            self.somma=self.somma-target
        return
            
