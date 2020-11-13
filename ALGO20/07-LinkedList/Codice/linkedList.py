class ListNode:
    def __init__(self,data):
        self.data=data
        self.next=None

    def __str__(self):
        return str(self.data)
    
class LinkedList:
    def __init__(self):
        self.head=None
        self.size=0

    def __len__(self):
        return self.size

    def __bool__(self):
        return len(self)>0

    def __contains__(self,item):
        curr=self.head
        while curr is not None:
            if item==curr.data:
                return True
            curr=curr.next
        return False
        
    def remove(self,target):
        prev=None
        curr=self.head
        
        while curr is not None and curr.data!=target:
            prev=curr
            curr=curr.next
    	
        if curr is None:
            return

        if curr is self.head:
            self.head=curr.next
        else:
            prev.next=curr.next

        self.size-=1


    def pop(self,index=None):
        if index==None:
            index=self.size-1

        if index<0:
            index+=self.size

        prev=None
        curr=self.head
        pos=0
        while pos!=index:
            prev=curr
            curr=curr.next
            pos+=1

        if curr is self.head:
            self.head=curr.next
        else:
            prev.next=curr.next

        self.size-=1
        return curr.data

      
    def __getitem__(self,index):
        if index<0:
            index+=self.size

        curr=self.head
        pos=0
        while curr is not None:
            if pos==index:
                return curr.data
            else:
                curr=curr.next
                pos+=1

        if curr is self.head:
            self.head=curr.next
        else:
            prev.next=curr.next

        self.size-=1
        return curr.data


    def __iter__(self):
    # nodo contenente l'elemento da restituire
        self.iter=self.head 
        return self


    # iteratore
    def __next__(self):
        if self.iter is None:
            raise StopIteration
        else:
            item=self.iter.data
            # ci spostiamo sul modo successivo
            self.iter = self.iter.next
        return item


    def insert(self,index,elem):
        newNode=ListNode(elem)

        if index<self.size:
            index=0
        
        if index>=self.size:
            index=self.size

        if index<0:
            index+=self.size


        prev=None
        curr=self.head
        pos=0
        while pos!=index:
            prev=curr
            curr=curr.next
            pos+=1

        if curr is self.head:
            newNode.next=self.head
            self.head=newNode
        else:
            prev.next=newNode
            newNode.next=curr

        self.size+=1
        

        

    def __str__(self):
        res='<'
        curr=self.head
        while curr is not None:
            res+=str(curr.data)
            curr=curr.next
            if curr is not None:
                res+=','
        res+='>'
        return res


    def insert_head(self,node):
        node.next=self.head
        self.head=node
        self.size+=1
