from bst import BST

T=BST()
T.insert("Italia","Roma")
T.insert("Francia","Parigi")
T.insert("Spagna","Madrid")
T.insert("Russia","Mosca")
T.insert("Giappone","Tokyo")
print("Visita inorder")
T.inorder()
print("\nVisita disorder")
T.disorder()
print("\nVisita inorder")
T.inorder()

