import random

class majority:
    
    def __init__(self):
        self.cnt=0
        self.element=None

    def addElement(self,a):
        if self.cnt==0:
            self.element=a
            self.cnt=1
        else:
            if self.element==a:
                self.cnt+=1
            else:
                self.cnt-=1


def main(lista):
    x=majority()
    for a in lista:
        x.addElement(a)
    return x.element

if __name__=='__main__':
    L=[2,3,4,4,4,1,2,7,8,4,4,9,4,4]
    print(L,main(L))

    L=[]
    N=10_000_000
    N2=N*2
    for i in range(N):
        L.append(random.randrange(N))
    s=random.randrange(N)
    print("Special element: ",s)
    ##add N copies of the special element
    for i in range(N):
        L.append(s)
    
    ##randomly permute the list 
    for i in range(N2-1):
        j=random.randrange(i+1,N2)
        L[i],L[j]=L[j],L[i]

    if (N<=100):
        print(L)

    print(main(L))
    
        
