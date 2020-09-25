#prima classe --
#una semplice classe con un attributo
#  i metodi costruttore
#  i metodi modificatori
#  un metodo lettore

class Ticker:

    #costruttore -- usato per costruire nuovi oggetti
    #numero massimo di persone viene passato come argomento
    
    def __init__(self):
        self.nprs=0

    #modificatori -- usati per modificare l'oggetto
    #se il numero di persone eccede il massimo non viene incrementato
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


