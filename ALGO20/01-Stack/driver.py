from stack import Stack
from stack import EmptyStack
    
#esempio di utilizzo della classe Stack
s = Stack([1,9,7])
print('Contenuto stack:', s)
size = len(s)
for _ in range(size+1):
    try:
        v = s.pop()
        print('top:', v)
    except EmptyStack as errore:
        print(errore)

print("Eseguo push di 4")
s.push(4)
print("Eseguo push di 4")
s.push(4)
print("Eseguo push di 1")
s.push(1)
print("Eseguo push di 2")
s.push(2)

print("Stampo lo stack")
print(s)

print("Ripulisco lo stack")
s.clear()
print(s)

print("Dopo aver ripulito lo stack")

if s:
    print('stack pieno')
else:
    print('stack vuoto')

print("Eseguo push di 4")
s.push(4)
print("Eseguo push di 23")
s.push(23)
print("Eseguo push di 1")
s.push(1)

lista = [1, 2]
for elemento in lista:
    if elemento in s:
        print(elemento, ' è nello stack')
    else:
        print(elemento, ' non è nello stack')

print('test iteratore')
print(s)
for element in s:
    print(element)

print('test copy')
ns = s

print('id(s): ', id(s), 's: ', s)
o = Stack([4, 23, 1])
print('id(o): ', id(o), 'o: ', o)

if s == o:
    print('Gli stack sono uguali')
else:
    print('Gli stack sono diversi')

print("Faccio push di 21 su o")
o.push(21)
print('id(s): ', id(s), 's: ', s)
print('id(o): ', id(o), 'o: ', o)
if s == o:
    print('Gli stack sono uguali')
else:
    print('Gli stack sono diversi')

if s != o:
    print('Gli stack sono diversi')
else:
    print('Gli stack sono uguali')


