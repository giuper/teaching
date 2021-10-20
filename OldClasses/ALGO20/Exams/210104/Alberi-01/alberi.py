class node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None

    def insert(self,val,path):

        if len(path)==0:  #sono arrivato a destinazione
            if val==self.data: #val==data --> nulla da fare
                pass
            else:
                self.data=val            #resettiamo data
            return
        
        if path[0]=='L': #devo andare a sinistra
            if self.left is None:   #a sinistra non c'e' niente
                self.left=node(val) #creo un nuovo nodo
                return              #diventa figlio sx di self
            else:                   
                self.left.insert(val,path[1:]) #ricorsivamente a sx
                return
        else:   #devo andare a destra
            if self.right is None:      #destra non c'e' nulla
                self.right=node(val)    #creo un nuovo nodo
                return                  #diventa figlio dx di self
            else:
                self.right.insert(val,path[1:]) #ricorsivamente a dx
                return

    def inorder(self):

        if self.left is not None:
            self.left.inorder()
            
        print(self.data)  
        
        if self.right is not None:
            self.right.inorder()

            
class tree:
    def __init__(self,val=None):
        self.root=None  
            

    def inorder(self):
        if self.root is None:
            return
        else:
            self.root.inorder()

    def insert(self,val,path=""):
        if self.root is None:  #se l'albero e' vuoto
            self.root=node(val)
            return
        if len(path)==0:
            if self.root.data==val:  #data=val --> nulla da fare
                pass
            else:
                self.root.data=val  #resettiamo data
        else:
            self.root.insert(val,path)

