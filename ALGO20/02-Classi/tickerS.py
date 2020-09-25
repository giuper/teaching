from tickerMF import TickerMF

class TickerS(TickerMF):

    def currentP(self):
        return self.currentM()+self.currentF()

    def setM(self,num):
        self.tm.set(num)

    def setF(self,num):
        self.tf.set(num)
    
    def __add__(self,other):
        res=TickerS()
        nM=self.currentM()+other.currentM()
        nF=self.currentF()+other.currentF()
        res.setM(nM)
        res.setF(nF)
        return res
    
    

    
