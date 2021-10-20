from bigNum import bigNum

class ltBigNum(bigNum):

    def __lt__(self,other):
        if len(self.list)<len(other.list):
            return True

        if len(self.list)>len(other.list):
            return False
        
#i due bignum hanno la stessa lunghezza
#costruiamo le liste AA e BB delle cifre dei due bignum
#a partire dalla piu' significativa alla meno significativa

        a=self.list.head
        b=other.list.head
        AA=[]
        BB=[]
        while (a is not None):
            AA.insert(0,a.data)
            BB.insert(0,b.data)
            a=a.next
            b=b.next


        for i in range(len(AA)):
            if AA[i]==BB[i]:
                continue
            return AA[i]<BB[i]
            
        return False
             
