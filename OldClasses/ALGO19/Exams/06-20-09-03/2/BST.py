class NODE:

    def __init__(self,k,v):
        self.key=k
        self.val=v
        self.left=None
        self.right=None

    def __str__(self):
        return str(self.key)+","+str(self.val)

class BST:

    def __init__(self):
        self.root=None

    def __ins(self,node,k,v):
        if node is None:
            newNode=NODE(k,v)
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

    def insert(self,k,v):
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

    def __del(self,node,k):
        if node is None:
            return None

        if k<node.key:
            node.left=self.__del(node.left,k)
            return node

        if k>node.key:
            node.right=self.__del(node.right,k)
            return node
        
        if node.left is None and node.right is None:
            return None

        if node.left is None and node.right is not None:
            return node.right

        if node.left is not None and node.right is None:
            return node.left
            
        [kmax,vmax]=self.__max(node.left)
        node.key=kmax
        node.val=vmax
        node.left=self.__del(node.left,kmax)
        return node


    def delete(self,k):
        self.root=self.__del(self.root,k)

        

