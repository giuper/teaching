#prima classe --
#una semplice classe con un attributo
#  i metodi costruttore
#  i metodi modificatori
#  un metodo lettore

class Ticker:

    #costruttore -- usato per costruire nuovi oggetti
    
    def __init__(self):
        self.nprs=0

    #modificatori -- usati per modificare l'oggetto
    def inc(self):
        self.nprs+=1

    def dec(self):
        if(self.nprs>0):
            self.nprs-=1

    def reset(self):
        self.nprs=0

    def set(self,num):
        self.nprs=num

    #lettore -- usato per leggere gli attributi dell'oggetto
    def current(self):
        return self.nprs


