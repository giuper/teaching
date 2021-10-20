from binari import BST

t=BST()
t.insert("Giustiniani, Andreolo",1385)
t.insert("Alighieri, Dante", 1265)
t.insert("Boccaccio, Giovanni", 1313)
t.insert("Petrarca, Francesco", 1304)
t.insert("Caracciolo, Bartolomeo", 1280)
t.insert("Polo, Marco", 1254)
t.insert("Coluccio Salutati, Lino", 1332)

t.inorder()
print ("l'alberto ha",len(t),"nodi")

