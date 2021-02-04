class nodeS:
    def __init__(self,k,v=None):
        if v is None:
            v=key
        self.key=k
        self.val=v
        self.left=None
        self.right=None

    def __str__(self):
        return "<"+str(self.key)+" -- "+str(self.val)+">"

    def __len__(self):
        if self.left is None:
            l=0
        else:
            l=len(self.left)

        if self.right is None:
            r=0
        else:
            r=len(self.right)
        return l+r+1

    def inorder(self):
        if self.left is not None:
            self.left.inorder()
        print(self)
        if self.right is not None:
            self.right.inorder()

    def disorder(self):
        if self.right is not None:
            self.right.disorder()
        print(self)
        if self.left is not None:
            self.left.disorder()

class BST:
    def __init__(self):
        self.root=None
            
    def __len__(self):
        if self.root is None:
            return 0
        else:
            return len(self.root)

    def inorder(self):
        if self.root is None:
            return
        else:
            self.root.inorder()

    def __ins(self,node,k,v):
        if node is None:
            newNode=nodeS(k,v)
            return newNode

        #node is not None
        #we found the key
        if node.key==k:
            node.val=v
            return node
        
        #the current key is larger than k--> go left
        if k<node.key:
            node.left=self.__ins(node.left,k,v)
            return node
        
        #the current key is smaller than k--> go right
        if k>node.key:
            node.right=self.__ins(node.right,k,v)
            return node

    def insert(self,k,v=None):
        if v==None:
            v=k
        self.root=self.__ins(self.root,k,v)


    def __in(self,node):
        if node is None:
            return 
        self.__in(node.left)
        print(node)
        self.__in(node.right)

    def inorder(self):
        self.__in(self.root)


    def __search(self,node,k):
        if node is None:
            return None

        if node.key==k:
            return node.val

        if k<node.key:
            return self.__search(node.left,k)

        if k>node.key:
            return self.__search(node.right,k)

    def search(self,k):
        return self.__search(self.root,k)
        
    def __max(self,node):
        if node.right is None:
            return [node.key,node.val] 
        else:
            return self.__max(node.right)

    def max(self):
        if self.root is not None:
            return self.__max(self.root)

    def disorder(self):
        if self.root is None:
            return
        else:
            self.root.disorder()


