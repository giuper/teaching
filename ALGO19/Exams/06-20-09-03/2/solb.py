from BST import BST


class solb(BST):


    def __somma(self,node):
        if node is None:
            return 0
        else:
            return self.__somma(node.left)+self.__somma(node.right)+node.val

    def somma(self):
        if self is not None:
                return self.__somma(self.root)
        else:
            return 0
            

