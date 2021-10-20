from bst import BST

iL=[100,50,25,75,150,180,280,380,120,121,118]
tL=[10,20,40,60,100,120,140,190,200]

T=BST()

for x in iL:
    T.insert(x)

print("Visita inorder")
T.inorder()

for t in tL:
    print(t,"-->",T.gt(t))

