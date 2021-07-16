from pLinkedList import PLinkedList

iHL=[10,4,8,4]
aL=[1000,11,12,3,1001]
iL=[[4,15],[2,1]]
pL=[4,5]
rL=[1000,12]

A=PLinkedList()

for x in iHL:
    print("insertHead(",x,")")
    A.insertHead(x)
    print("Lista:",A)
    print("Numero elementi pari e Lunghezza: ",A.pari,A.size)
    print()

for x in aL:
    print("append(",x,")")
    A.append(x)
    print("Lista:",A)
    print("Numero elementi pari e Lunghezza: ",A.pari,A.size)
    print()
    
for x in iL:
    print("insert(",x,")")
    [idx,el]=x
    A.insert(idx,el)
    print("Lista:",A)
    print("Numero elementi pari e Lunghezza: ",A.pari,A.size)
    print()

for x in pL:
    print("pop(",x,")")
    print(A.pop(x))
    print("Lista:",A)
    print("Numero elementi pari e Lunghezza: ",A.pari,A.size)
    print()

for x in rL:
    print("remove(",x,")")
    A.remove(x)
    print("Lista:",A)
    print("Numero elementi pari e Lunghezza: ",A.pari,A.size)
    print()
    
    
