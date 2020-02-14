
from BST import BST

class SBST(BST):

    def __min(self,node):
        if node.left is None:
            return [node.key,node.val] 
        else:
            return self.__min(node.left)

    def min(self):
        if self.root is not None:
            return self.__min(self.root)


#assumiamo che l'albero contenga almeno due nodi
    def smin(self):
        if self.root.left is None:
            return self.__min(self.root.right)
        else:
            return self._smin(self.root)

    def _smin(self,node):
        if node.left is None:
            if node.right is None:
                return None
            else:
                return self.__min(node.right)
        ris=self._smin(node.left)
        if ris is None:
            return [node.key,node.val]
        else:
            return ris
            
        
