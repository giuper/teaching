##sparse matrix with sorted list of elements

class matrixElement:

    def __init__(self,r,c,v=0):
        self.row=r
        self.col=c
        self.val=v

    def __eq__(self,other):
        return self.row==other.row and self.col==other.col

    def __lt__(self,other):
        if self.row<other.row:
            return True
        if self.row==other.row and self.col<other.col:
            return True
        else:
            return False
           
class SparseMatrix:

    def __init__(self,r,c):
        self.row=r
        self.col=c
        self._elements=list()
##to be removed in final version
        self._elements=[matrixElement(2,3,9),\
                        matrixElement(2,5,99),\
                        matrixElement(3,4,999)]

##modified Binary Search 
##if x is in the list of elements
## it returns the index
##else
## it returns where it should be
    def _BS(self,x):
        l=0
        h=len(self._elements)-1
        while l<=h:
            m=(h+l)//2
            if self._elements[m]==x:
                return m
            if x<self._elements[m]:
                h=m-1
            else:
                l=m+1

        return l

    def __getitem__(self,ind):
#aggiungere controlli sugli indici
        row=ind[0]
        col=ind[1]
        x=matrixElement(row,col)
        indx=self._BS(x)
        if self._elements[indx]==x:
            return self._elements[indx].val
        else:
            return 0

##aggiungere setitem
##           add
##           mult
    
A=SparseMatrix(10,10)
print(A[2,3])
print(A[3,3])





