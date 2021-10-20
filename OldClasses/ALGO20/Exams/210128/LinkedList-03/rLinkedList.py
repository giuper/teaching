from stack import Stack
from linkedList import LinkedList

class rLinkedList(LinkedList):

    def reverse(self):
        s=Stack()
        for x in self:
            s.push(x)

        rL=rLinkedList()
        while s:
            x=s.pop() 
            rL.append(x)
        return rL
        

