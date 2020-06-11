from BST import BST


class SBST(BST):

    def min(self,node):
        while node.left is not None:
            node=node.left
        return node

    def sorting(self):
        SBST=self
        nodo=SBST.root
        output=list()
        while nodo is not None:
            minimo=SBST.min(nodo)
            output.append(minimo.val)
            SBST.root=BST.delete(nodo,minimo.key)
            nodo=SBST.root
        return output
