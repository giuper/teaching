from linkedList import LinkedList

class AddLinkedList(LinkedList):

    def __add__(self,other):
        res=LinkedList()
        a=self.head
        b=other.head
        
        while (a is not None) and (b is not None):
            res.append(min(a.data,b.data))
            a=a.next
            b=b.next

        while (a is not None):
            res.append(a.data)
            a=a.next

        while (b is not None):
            res.append(b.data)
            b=b.next

        return res
        
