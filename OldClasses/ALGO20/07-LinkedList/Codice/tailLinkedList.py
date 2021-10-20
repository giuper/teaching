from linkedList import LinkedList
from linkedList import ListNode

class TailLinkedList(LinkedList):
    
    def __init__(self):
        super().__init__()
        self.tail=None

    def append(self,element):
        newNode=ListNode(element)
        if self.size==0:
            self.head=newNode
        else:
            self.tail.next=newNode
        self.tail=newNode
        self.size += 1

    def insertHead(self,element):
        newNode=ListNode(element)
        newNode.next=self.head
        self.head=newNode
        if self.size==0:        #se la lista era vuota
            self.tail=newNode   #newNode e' anche l'ultimo elemento
        self.size+=1
        
    def insert(self,index,element):
#inserisci un nuovo nodo contentente element come data
#in modo tale che al termine della insert
#il nuovo nodo ha indice uguale a index
        
        #se index=0,...,len(self)-1  --> index conta dal primo
        
        if index<-self.size: #ci dovrebbe essere un errore
            index=0          #scegliamo di accedere al primo elemento
            
        if index>=self.size: #ci dovrebbe essere un errore
            index=self.size  #scegliamo di aggiungere element come ultimo

        #se index=-1,...,-len(self)  --> index conta dall'ultimo
        #                                equivalent ad aggiungere len(self)    
        if index<0:         #riportiamo l'indice negativo al range [0,len(self)-1]
            index+=self.size

        predNode=None
        curNode=self.head
        pos=0
        while pos!=index:
            predNode=curNode
            curNode=curNode.next
            pos +=1

        if curNode is self.head:  #index=0 e quindi insert e' una insertHead
            self.insertHead(element)
            return

        if curNode is None:  #index=self.size e quindi la insert e' una append
            self.append(element)
            return
        
        #se arrivo qui la insert non e' ne' in testa ne' in coda
        newNode=ListNode(element)
        predNode.next=newNode
        newNode.next=curNode
        self.size+=1
        
    def remove(self,target):

        predNode=None
        curNode=self.head
    
        while curNode is not None and curNode.data!=target:
            predNode=curNode
            curNode=curNode.next
    	
        if curNode is None:
            return

        if len(self)==1:    #devo cancellare l'unico elemento della lista
            self.head=None  #la lista risultante e' vuota
            self.tail=None
            self.size-=1
            return
        
       #se arrivo qui, la lista ha piu' di 1 elemento 

        self.size-=1                
        if curNode is self.head: #sto cancellando il primo
            self.head=curNode.next
            return

        if curNode is self.tail: #sto cancellando l'ultimo
            self.tail=predNode
            predNode.next=None
            return

        #sto cancellando un nodo intermedio
        predNode.next=curNode.next
        
