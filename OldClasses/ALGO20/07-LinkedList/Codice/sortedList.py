from linkedList import LinkedList
from linkedList import ListNode

class Sorted(LinkedList):
    
    def insert(self,element):

        newNode=ListNode(element)

        if self.size==0:
            self.head=newNode
            self.size=1
            return

        predNode=None
        curNode=self.head
        
        while curNode is not None and curNode.data<=newNode.data:
            predNode=curNode
            curNode=curNode.next

        if curNode is self.head:
            newNode.next=self.head
            self.head=newNode
        else:
            predNode.next=newNode
            newNode.next=curNode

        self.size+=1


