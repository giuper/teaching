##primo esempio di classe
##costruzione
##consultazione
##modifica

class Studenti:

    def __init__(self,nome,cognome,cds):
        
        self.nome=nome
        self.cognome=cognome
        self.cds=cds
        self.cfu=0

    def getNome(self):
        return self.nome

    def getCognome(self):
        return self.cognome

    def getCFU(self):
        return self.cfu

    def getCDS(self):
        return self.cds

    def setCDS(self,cdsNuovo):
        self.cds=cdsNuovo

    def setCFU(self,cfuNuovo):
        self.cfu=cfuNuovo

    def addCFU(self,cfuEsameSuperato):
        self.cfu+=cfuEsameSuperato
    
##fine classe


x=Studenti("Gianfranco","Rossi","Lettere")
print (x.getNome())
print (x.nome)  #pericolo!!!  
print (x.getCognome())
print (x.getCFU())
print (x.getCDS())
x.setCDS("Statistica per Big Data")
print (x.getCDS())

print ("Lo studente supera ASD")
x.addCFU(10)
print (x.getCFU())
