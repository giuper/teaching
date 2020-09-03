from BST import BST


class solm(BST):


    def __depth(self,node):
        if node is None:
            return 0
        else:
            return 1+max(self.__depth(node.left),self.__depth(node.right))

    def depth(self):
        if self is not None:
                return self.__depth(self.root)
        else:
            return 0
            

