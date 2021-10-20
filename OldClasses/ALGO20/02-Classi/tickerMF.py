#questa classe ha piu' attributi
#che sono oggetti di un'altra classe

# vogliamo un ticker che conti separatamente maschi e femmine

from ticker import Ticker

class TickerMF:

    #costruttore -- usato per costruire nuovi oggetti

    def __init__(self):
        self.tm=Ticker()
        self.tf=Ticker()

        
    #modificatori -- usati per modificare gli oggetti

    def incM(self):
        self.tm.inc()

    def incF(self):
        self.tf.inc()
        
    def decM(self):
        self.tm.dec()

    def decF(self):
        self.tf.dec()

    def reset(self):
        self.tf.reset()
        self.tm.reset()

    #lettori -- usati per leggere gli attributi degli oggeti

    def currentM(self):
        return self.tm.current()

    def currentF(self):
        return self.tf.current()
    
