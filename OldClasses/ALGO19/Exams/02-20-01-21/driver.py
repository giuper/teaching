from sol import Bag1
##modificare inserendo il nome del file come specificato
##dalla traccia

print("Fase I")
B=Bag1()
B.add1(12)
B.add1(21)
B.add1(7)
B.add1(7)
B.add1(7)

print("Contiene ",len(B),"elementi")
print("\tminimo:\t",B.Min())

print("Elenco elementi in ordine crescente")
for x in B:
    print(x)
print("Lista elementi presenti in ordine di inserimento e con ripetizioni")
print(B.timeAdded())

print("\n\nFase II")
B.add(7)
print("Adesso contiene ",len(B),"elementi")
print("\tminimo:\t",B.Min())

print("Elenco elementi")
for x in B:
    print(x)
print("Lista elementi presenti in ordine di inserimento e con ripetizioni")
print(B.timeAdded())

print("\n\nFase III")
B.add1(1000)
B.add1(1)
print("\nAdesso contiene ",len(B),"elementi")
print("\tminimo:\t",B.Min())

print("Elenco elementi")
for x in B:
    print(x)
print("Lista elementi presenti in ordine di inserimento e con ripetizioni",B.timeAdded())


B=Bag1()
for x in range(1000):
    B.add1(x)
    B.add1(x)
    B.add1(x)
    B.add(x)

print("\nContiene ",len(B),"elementi")
tuttobene=True
for x in range(1000):
    if x not in B:
        tuttobene=False
        print("Manca ",x)

if tuttobene:
    print("Non manca nulla")
B.add1(-1)
B.add1(10000)
print("\tminimo:\t",B.Min())

