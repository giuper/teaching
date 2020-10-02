class EmptyStack(Exception):
    # Variabile di classe
    _msg = 'Stack vuoto'

    def __str__(self):
        return EmptyStack._msg

# Classe usata da python quando si trova ad eseguire
# for x in s per un oggetto s della classe Stack

class StackIter:

    def __init__(self,sequence):
        self.items=sequence
        self.cur=0

    def __iter__(self):
        return self

    def __next__(self):
        if self.cur<len(self.items):
            item=self.items[self.cur]
            self.cur=self.cur+1
            return item
        else:
            raise StopIteration
       

class Stack:
    # Riceve un iterable e inserisce i suoi elementi,
    # a partire dalla posizione 0, nello stack
    
    def __init__(self,sequence=None):
        # rappresentiamo lo stack con una lista
        # il top è la fine della lista
        # sequence  = None crea uno stack vuoto
        if sequence == None:
            sequence = list()
        self._container = list()
        for element in sequence:
            self._container.append(element)
            
    # Se lo stack è vuoto lancia un’eccezione
    # Rimuove l’elemento al top dello stack
    # Restituisce l’elemento eliminato
    def pop(self):
        if self.is_empty():
            raise EmptyStack
        else:
            return self._container.pop(len(self._container) - 1)

    # Restituisce l’elemento al top dello stack
    # Se lo stack è vuoto lancia un’eccezione
    def peek(self):
        if self.is_empty():
            raise EmptyStack
        else:
            return self._container[len(self._container) - 1]

    # Inserisce l'elemento item al top dello stack
    def push(self, item):
        self._container.append(item)

    #  Restituisce true se lo stack è vuoto, false altrimenti
    def is_empty(self):
        if self._container:
            return False
        else:
            return True
        ##equivalente
        ## return not self._container

    # Cancella tutti gli elementi contenuti nello stack
    def clear(self):
        self._container = []

    # Restituisce una versione stampabile dello stack
    # Usata da python quando deve eseguire print(self) 
    # per un oggetto self delle classe Stack

    def __str__(self):
        if self.is_empty():
            return '<>'
        else:
            return '<' + str(self._container) + ', top: '+ str(self.peek()) + '>'


    # Restituisce il numero degli elementi contenuti nello stack
    # Usata da python quando deve eseguire len(self) 
    # per un oggetto self delle classe Stack
    def __len__(self):
        return len(self._container)

    # Usata da python quando deve assegnare un valore Booleano
    # ad un oggetto self delle classe Stack
    # Restituisce true se lo stack non è vuoto, false altrimenti
    def __bool__(self):
        return len(self._container)>0
    ##return self._container


    # Usata da python quando deve valutare l'espressione Booleana
    # x in self 
    # per un oggetto self delle classe Stack
    # Restituisce true se item è contenuto nello stack, false altrimenti
    def __contains__(self,item):
        return item in self._container

    # Costruisce un iteratore per self
    def __iter__(self):
        return StackIter(self._container)


    # Usata da python quando deve assegnare self ad una variabile
    # Restituisce una copia dello stack
    def __copy__(self):
        newSelf=Stack()
        for x in self:
            newSelf.push(x)
        return newSelf
    
    # Usata da python per valutare l'espressione Booleana
    # self==other
    # Restituisce true se lo stack other contiene gli stessi elementi
    # dello stack self
    def __eq__(self, other):
        if len(self)!=len(other):
            return False
        for i in range(len(self)):
            if self._container[i]!=other._container[i]:
                return False
        return True

    # Usata da python per valutare l'espressione Booleana
    # self!=other
    # Restituisce true se lo stack other è diverso dallo stack self
    def __ne__(self, other):
        return not self==other

