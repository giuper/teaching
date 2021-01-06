from linkedList import LinkedList

class Sol(LinkedList):

    def nuovo(self,verbose=False):
        B=LinkedList()
        prev=None
        for x in self:
            if verbose:
                print("Prev-Curr",prev,x)
            if prev is not None:
                B.append([x[0],x[1]-prev])
                if verbose:
                    print("\tinserting:",x[0],x[1]-prev)
            else:
                if verbose:
                    print("\tNot inserting anything")
                else:
                    pass
            prev=x[1]
        
        return(B)
