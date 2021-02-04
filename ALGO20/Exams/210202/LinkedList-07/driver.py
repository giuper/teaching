from mLinkedList import MLinkedList

iHL=[10,40,20,40]
aL=[1000,11,12,13,1001]
iL=[[4,15],[8,15000]]
A=MLinkedList()

for x in iHL:
    A.insertHead(x)
    print("Lista:",A)
    print("Massimo e Lunghezza: ",A.max,A.size)

for x in aL:
    A.append(x)
    print("Lista:",A)
    print("Massimo e Lunghezza: ",A.max,A.size)
    
for x in iL:
    [idx,el]=x
    A.insert(idx,el)
    print("Lista:",A)
    print("Massimo e Lunghezza: ",A.max,A.size)


