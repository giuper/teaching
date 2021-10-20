from lbst import lBST

t=lBST()
t.insert("aaaa")
t.insert("abaa")
t.insert("aaca")
t.insert("aaad")
t.insert("abcd")
print("Inserisco 5 stringhe di lunghezza 4")
print ("l'albero ha",len(t),"nodo contenente una lista di 5 stringhe")
t.inorder()
print()
print()

t.insert("bc")
t.insert("abcddf")
t.insert("bcd")
t.insert("b")
t.insert("abcdd")
t.insert("abcddfg")

print("Inserisco delle stringhe ed effettuo la visita inorder")
t.inorder()
print ("l'albero ha",len(t),"nodi\n\n")

t.insert("aacd")
t.insert("ac")
t.insert("aacddf")
t.insert("acd")
t.insert("a")
t.insert("aacdd")
t.insert("aacddfg")

print("Inserisco delle altre stringhe ed effettuo la visita inorder")
t.inorder()
print("Notare che le stringhe della stessa lunghezza sono nello stesso nodo")
print("che ha come chiave la lunghezza delle stringhe")
print ("l'albero ha",len(t),"nodi\n\n")



