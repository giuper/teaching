from bigNum import bigNum

class eqbigNum(bigNum):

    def __eq__(self,other):
        a=self.list.head
        b=other.list.head
        while (a is not None) and (b is not None):
            if a.data != b.data:
                return False
            a=a.next
            b=b.next

        return (a is None and b is None)
            
             
