
class SparseMatrix:
    class _MatrixElement:
        def __init__(self, row, col, value):
            self._row=row
            self._col=col
            self._value=value

        def __str__(self):
            return "["+str(self._row)+","+str(self._col)+"]="+str(self._value)+"\n"

    
# Crea una matrice numRows x numCols sparsa inizializzata a 0
    def __init__(self, numRows, numCols):
        self._numRows=numRows
        self._numCols=numCols
        self._elementList=list()


# Restituisce il numero di righe della matrice
    def numRows( self ): 
        return self._numRows

# Restituisce il numero di colonne della matrice
    def numCols( self ): 
        return self._numCols

# Restituisce l'elemento della matrict a riga row e colonna col
    def _findPosition(self, row, col):
        i=0
        for element in self._elementList:
            if row==element._row and col==element._col:
                return i
            i+=1
        return None


#Pone il valore alla posizione ndxTuple uguale a scalar
    def __setitem__(self, ndxTuple, scalar):
        ndx=self._findPosition(ndxTuple[0],ndxTuple[1])
       
        if ndx is not None: # se l'elemento è trovato in _elementList
            # se il nuovo valore è diverso da zero, modifichiamo quello vecchio
            if scalar != 0.0:
                self._elementList[ndx]._value=scalar
            else: #altrimenti rimuoviamo l'elemento da _elementList
                self._elementList.pop(ndx)
        else: # se l'elemento non nella lista ed è diverso da zero
            if scalar!=0.0 :
            # aggiungiamo l'elemento a _elementList
                element=self._MatrixElement(ndxTuple[0], ndxTuple[1], scalar)
                self._elementList.append(element)

# Restituisce il valore dell'elemento (i, j), x[i, j]
    def __getitem__(self, ndxTuple):
        ndx = self._findPosition(ndxTuple[0], ndxTuple[1])
        return self._elementList[ndx]._value if ndx != None else 0

    def __add__(self, B):
        assert B.numRows() == self.numRows() and \
               B.numCols() == self.numCols(), \
               "Le matrici non sono compatibili per essere addizionate."

        # Creare la nuova matrice.
        N=SparseMatrix(self.numRows(), self.numCols())

        # Duplicare la matrice self, _MatrixElement è mutable, non
        # possiamo semplicemente copiare il riferimento

        for elemento in self._elementList :
                dupElement=self._MatrixElement(elemento._row, elemento._col, elemento._value)
                N._elementList.append(dupElement)

        # Iterare sugli elementi diversi da zero della matrice B
        for elemento in B._elementList :
            # Prendere il corrispondente valore
            valore=N[elemento._row,elemento._col]
            valore += elemento._value
            # Memorizzare il nuovo valore nella nuova matrice
            N[elemento._row, elemento._col]=valore

        # Restituire la nuova matrice
        return N
  
    def __str__(self):
        res=""
        for elemento in self._elementList:
            res=res+str(elemento)
        return res
