from LLmax import LLmax

A=LLmax()
print("Lista: ",A)
print("Massimo: ",A.massimo())
print()

A.append(12)
A.append(3)
A.append(45)
A.insert(2,8)
print("Lista: ",A)
print("Massimo: ",A.massimo())

print()
print("Faccio pop")
print("Risultato: ",A.pop())
print("Lista: ",A)
print("Massimo: ",A.massimo())

print()
print("Faccio remove di 3")
A.remove(3)
print("Lista: ",A)
print("Massimo: ",A.massimo())

print()
print("Faccio remove di 7")
A.remove(7)
print("Lista: ",A)
print("Massimo: ",A.massimo())

