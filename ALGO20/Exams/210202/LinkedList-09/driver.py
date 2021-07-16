from tLinkedList import TLinkedList

iHL=[10,4,8,4,83,18,94,51]
aL=[1000,11,120,3,1001]
iL=[[4,15],[2,1]]
pL=[4,5]
rL=[1000,12]

A=TLinkedList(50)

for x in iHL:
    print("insertHead(",x,")")
    A.insertHead(x)
    print("Lista (t):",A,"(",A.t,")")
    print("Numero tentativi e lunghezza: ",A.tries,A.size)
    print()

for x in aL:
    print("append(",x,")")
    A.append(x)
    print("Lista (t):",A,"(",A.t,")")
    print("Numero tentativi e lunghezza: ",A.tries,A.size)
    print()
    
for x in iL:
    print("insert(",x,")")
    [idx,el]=x
    A.insert(idx,el)
    print("Lista (t):",A,"(",A.t,")")
    print("Numero tentativi e lunghezza: ",A.tries,A.size)
    print()

for x in pL:
    print("pop(",x,")")
    print(A.pop(x))
    print("Lista (t):",A,"(",A.t,")")
    print("Numero tentativi e lunghezza: ",A.tries,A.size)
    print()

for x in rL:
    print("remove(",x,")")
    A.remove(x)
    print("Lista (t):",A,"(",A.t,")")
    print("Numero tentativi e lunghezza: ",A.tries,A.size)
    print()
    
    
