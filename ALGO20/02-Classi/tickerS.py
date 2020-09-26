from tickerMF import TickerMF

class MaxCapacity(Exception):

    def __str__(self):
        return "Massima capacita' raggiunta"

class TickerS(TickerMF):

    def __init__(self,mas):
        super().__init__()
        self.mas=mas

    def incF(self):
        if self.currentP()<self.mas:
            self.tm.inc()
        else:
            raise MaxCapacity

    def incM(self):
        if self.currentP()<self.mas:
            self.tm.inc()
        else:
            raise MaxCapacity
        
    def currentP(self):
        return self.currentM()+self.currentF()

    def setM(self,num):
        self.tm.set(num)

    def setF(self,num):
        self.tf.set(num)
    
    def __add__(self,other):
        nM=self.currentM()+other.currentM()
        nF=self.currentF()+other.currentF()
        if nM+nF>self.mas:
            raise MaxCapacity
        else:
            res=TickerS(self.mas)
            res.setM(nM)
            res.setF(nF)
            return res
    
    

    
