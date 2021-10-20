class node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None

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

    def insert(self,path,val):
        if path[0]=='L':
            if self.left is None:
                new=node(val)
                self.left=new
            else:
                self.left=self.left.insert(path[1:],val)
        if path[0]=='R':
            if self.right is None:
                new=node(val)
                self.right=new
            else:
                self.right=self.right.insert(path[1:],val)

        return self

    def inorder(self):
        if self.left is not None:
            self.left.inorder()
        print(self.data)
        if self.right is not None:
            self.right.inorder()

class tree:
    def __init__(self,val=None):
        if val is None:
            self.root=None
        else:
            self.root=node(val)
            
    def __len__(self):
        if self.root is None:
            return 0
        else:
            return len(self.root)

    def insert(self,path,val):
        if self.root is None:
            self.root=node(val)
        else:
            self.root.insert(path,val)

    def inorder(self):
        if self.root is None:
            return
        else:
            self.root.inorder()
            







        
    
