from BST import BST


class solt(BST):


    def __size(self,node):
        if node is None:
            return 0
        else:
            return self.__size(node.left)+self.__size(node.right)+1

    def size(self):
        if self is not None:
                return self.__size(self.root)
        else:
            return 0
            

