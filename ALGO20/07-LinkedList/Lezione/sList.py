from linkedList import LinkedList
from linkedList import ListNode


#una lista in cui i nodi hanno i campi data ordinati
#in ordine non decrescente

class SortedList(LinkedList):

#inserisce un nuovo nodo contenente element
#in una lista ordinata
#in un modo da mantenere l'ordine non decrescente
    
    def insert(self,element):

        newNode=ListNode(element)
        
        if self.head is None: #la lista e' vuota
            self.head=newNode
            self.size+=1
            return

        pred=None
        curr=self.head

        while curr is not None and curr.data<=element:
            pred=curr
            curr=curr.next

        #inserisco newNode tra pred e curr
        #prima:   pred-->curr 
        #dopo:    pred-->newNode-->curr

        if pred is not None:

        #    Prima: 
        #    pred    curr        newNode
        #    20 -->  25           23
        #    pred.next=curr       newNode.next=None

        #    Dopo: 
        #    pred     newNode       curr
        #     20  -->   23     -->   25


            pred.next=newNode
            newNode.next=curr
            self.size+=1
            
        else:
            ## pred is None
            ## Prima:
            ## self.head -->    curr
            
            ## Dopo:
            ## self.head  --> newNode --> curr
            self.head=newNode
            newNode.next=curr
            self.size+=1
            
        return
    
        
        
        


            
        
    
