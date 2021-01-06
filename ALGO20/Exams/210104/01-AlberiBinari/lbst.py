from bst import BST
from bst import nodeS

class lBST(BST):
    def __ins(self,node,k,v):
        if node is None:
            newNode=nodeS(k,v)
            return newNode

        #node is not None
        #we found the key
        if node.key==k:
            if v[0] not in node.val:  ##
                node.val=node.val+v   ##
            return node
        
        #the current key is larger than k--> go left
        if k<node.key:
            node.left=self.__ins(node.left,k,v)
            return node
        
        #the current key is smaller than k--> go right
        if k>node.key:
            node.right=self.__ins(node.right,k,v)
            return node

    def insert(self,v):
        self.root=self.__ins(self.root,len(v),[v])  ##


