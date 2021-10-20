class ListNode:

    def __init__(self,data):
        self.data=data
        self.next=None


class LinkedList:

    def __init__(self):
        self.head=None
        self.size=0

    def stampa(self):
        cur=self.head
        while cur is not None:
            print(cur.data)
            cur=cur.next

    def __oldlen__(self): #O(n), n=numero elementi nella lista
        size=0
        cur=self.head
        while cur is not None:
            size+=1
            cur=cur.next
        return size

    def __len__(self): #O(1)
        return self.size


    def __contains__(self, item):  #O(n), n=numero elementi nella lista
        curNode = self.head
        while curNode is not None:
            if item == curNode.data:
                return True
            curNode = curNode.next
        return False
#cerca il nodo che ha data=target
#se lo trovi lo rimuovi dalla lista
    
    def remove(self,target):
        prevNode=None
        curNode=self.head
        while curNode is not None and curNode.data!=target:
            prevNode=curNode
            curNode=curNode.next

        if curNode is None: #non ho trovato alcun nodo con data=target
            return

        #ho trovato nodo con data=target
        if curNode is self.head:
            self.head=curNode.next
        else:
            prevNode.next=curNode.next

        self.size-=1
        

        
        
    def insert(self,nodo): #O(1)
        #inserisci nodo come primo elemento della lista self
        nodo.next=self.head
        self.head=nodo
        self.size+=1
    
##       Esempio:
##       Lista self prima inserimento --->   self.head-->2-->52-->18-->36-->13
##       inserire un nodo che ha valore 44
##       Lista self dopo inserimento  --->  self.head-->44-->2 52 18 36 13 

            
##a=ListNode(2)
##b=ListNode(52)
##c=ListNode(18)
##d=ListNode(36)
##e=ListNode(13)
##a.next=b
##b.next=c
##c.next=d
##d.next=e

##L=LinkedList()
##L.head=a
#a=b=c=d=e=None




