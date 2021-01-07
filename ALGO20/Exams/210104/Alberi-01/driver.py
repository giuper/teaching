from sol import tree

T=tree()
print("Inseriamo dei valori")
T.insert("Z")
T.insert("G","R")
T.insert("C","L")
T.insert("O","RR")
T.insert("Cl","RL")
T.insert("S","LL")
T.insert("Ct","LR")
print("Eseguiamo la inorder e notiamo che tutti i valori hanno count=1")
T.inorder()

print()

print("Inseriamo S a LL di nuovo")
T.insert("S","LL")
print("Eseguiamo la inorder e notiamo che S ha count=2")
T.inorder()

print()

print("Inseriamo Ct a LR per altre due volte")
T.insert("Ct","LR")
T.insert("Ct","LR")
print("Eseguiamo la inorder e notiamo che Ct ha count=3")
T.inorder()

print()

print("Inseriamo Sc a LL")
T.insert("Sc","LL")
print("Eseguiamo la inorder e notiamo che Sc ha count=1")
T.inorder()

