class ListNode:
    def __init__(self,data):
        self.data=data
        self.next=None


class LinkedList:
    def __init__(self):
        self.head=None
        self.size=0

    def __len__(self):
        return self.size

    def __bool__(self):
        return len(self)>0

    def __contains__(self,item):
        curNode=self.head
        while curNode is not None:
            if item==curNode.data:
                return True
            curNode=curNode.next
        return False
        
    def remove(self,target):
        predNode=None
        curNode=self.head
    
        while curNode is not None and curNode.data!=target:
            predNode=curNode
            curNode=curNode.next
    	
        if curNode is None:
            return

        if curNode is self.head:
            self.head=curNode.next
        else:
            predNode.next=curNode.next

        self.size-=1

    def pop(self,index=None):
        if index==None:
            index=self.size-1

        if index<0:
            index+=self.size

        predNode=None
        curNode=self.head
        pos=0
        while pos!=index:
            predNode=curNode
            curNode=curNode.next
            pos+=1

        if curNode is self.head:
            self.head=curNode.next
        else:
            predNode.next=curNode.next

        self.size-=1
        return curNode.data

      
    def __getitem__(self,index):
        if index<0:
            index+=self.size

        curNode=self.head
        pos=0
        while curNode is not None:
            if pos==index:
                return curNode.data
            else:
                curNode=curNode.next
                pos+=1

        if curNode is self.head:
            self.head=curNode.next
        else:
            predNode.next=curNode.next

        self.size-=1
        return curNode.data


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


    def append(self,elem):
        self.insert(len(self),elem)

    def insert(self,index,elem):
        newNode=ListNode(elem)

        if index<self.size:
            index=0
        
        if index>=self.size:
            index=self.size

        if index<0:
            index+=self.size


        predNode=None
        curNode=self.head
        pos=0
        while pos!=index:
            predNode=curNode
            curNode=curNode.next
            pos+=1

        if curNode is self.head:
            newNode.next=self.head
            self.head=newNode
        else:
            predNode.next=newNode
            newNode.next=curNode

        self.size+=1
        

    def __str__(self):
        res='<'
        curNode=self.head
        while curNode is not None:
            res+=str(curNode.data)
            curNode=curNode.next
            if curNode is not None:
                res+=','
        res+='>'
        return res


    def insertHead(self,element):
        new_node=ListNode(element)
        new_node.next=self.head
        self.head=new_node
        self.size+=1

