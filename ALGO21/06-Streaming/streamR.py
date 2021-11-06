import random

class randomSelection():

    def __init__(self):
        self.r=None
        self.s=0

    def addElement(self,a,c):
        if self.r is None:
            self.r=a
            self.s=c
        else:
            self.s+=c
            x=random.randrange(self.s)
            if x<c:
                self.r=a

def main():
    L=[(1,23),(2,12),(7,1),(9,4),(5,110),(6,1),(2,3)]
    x=randomSelection()
    for a,c in L:
        x.addElement(a,c)
        print("Random element: ",x.r)
        print("Total sum:      ",x.s)
    

if __name__=='__main__':
    main()
    
