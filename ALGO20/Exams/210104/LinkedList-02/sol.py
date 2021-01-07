from linkedList import LinkedList

class Sol(LinkedList):

    def nuovo(self):
        B=LinkedList()
        prev=0
        for x in self:
            prev=prev+x[1]
            B.append([x[0],prev])
        
        return(B)
