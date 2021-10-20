from linkedList import LinkedList

class LLmax(LinkedList):

    def massimo(self):
        if self.head is None:
            return 0
        cmax=self.head.data
        curNode=self.head
        while curNode.next is not None:
            curNode=curNode.next
            if curNode.data>cmax:
                cmax=curNode.data

        return cmax
            
