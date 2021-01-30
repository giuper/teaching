class node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None

    def __len__(self):
        #calcolo numero nodi a sx
        if self.left is None:
            l=0
        else:
            l=len(self.left)
            
        #calcolo numero nodi a dx
        if self.right is None:
            r=0
        else:
            r=len(self.right)

        return 1+l+r

    def height(self):
        #calcolo altezza di sx
        if self.left is None:
            l=0
        else:
            l=self.left.height()

        #calcolo altezza di dx
        if self.right is None:
            r=0
        else:
            r=self.right.height()

        return 1+max(l,r)

    
        
    def inorder(self):

        if self.left is not None:
            self.left.inorder()
            
        print(self.data)
        
        if self.right is not None:
            self.right.inorder()



    def insert(self,val,path,theTree):

        if len(path)==0:  #sono arrivato a destinazione
            self.data=val
            return
        
        if path[0]=='L': #devo andare a sinistra
            if self.left is None:   #a sinistra non c'e' niente
                self.left=node(val) #creo un nuovo nodo
                theTree.size+=1
                return              #diventa figlio sx di self
            else:                   
                self.left.insert(val,path[1:],theTree) #ricorsivamente a sx
                return
        else: 
            if self.right is None:
                self.right=node(val)
                theTree.size+=1
                return
            else:
                self.right.insert(val,path[1:],theTree)
                return
            
class tree:
    def __init__(self,val=None):
        if val is None:
            self.root=None
            self.size=0
        else:
            self.root=node(val)
            self.size=1
            
    def __len__(self):
        if self.root is None:
            return 0
        else:
            return len(self.root)

    def height(self):
        if self.root is None:
            return 0
        else:
            return self.root.height()

    def inorder(self):
        if self.root is None:
            return
        else:
            self.root.inorder()

    def insert(self,val,path=""):
        if self.root is None:  #se l'albero e' vuoto
            newNode=node(val)
            self.root=newNode  #newNode ne diventa la radice
            self.size=1
        self.root.insert(val,path,self)

