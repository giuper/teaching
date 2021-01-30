from numsx import tree


T=tree()
T.insert(91,"")
T.insert(77,"L")
T.insert(33,"LL")
T.insert(54,"LLR")
T.insert(9,"LR")
T.insert(3,"R")
T.insert(1,"RL")
T.insert(5,"RR")

print("Albero: ")


print("                       91 ")
print("                      /  \ ")
print("                     /    \ ")
print("                    77     3")
print("                   / \    / \ ")
print("                  /   \   | | ")
print("                 33    9  1 5")
print("                  \ ")
print("                   54")

print("Con inorder")
T.inorder()
print("L'albero contiene",T.numSx(),"nodi con solo figlio sinistro")
print("\nEseguiamo di nuovo la visita inorder")
T.inorder()

T=tree()
T.insert(91,"")
T.insert(77,"L")
T.insert(33,"LL")
T.insert(54,"LLL")
T.insert(9,"LR")
T.insert(3,"R")
T.insert(1,"RL")

print()
print()
print("Albero: ")


print("                       91 ")
print("                      /  \ ")
print("                     /    \ ")
print("                    77     3")
print("                   / \    / ")
print("                  /   \   |  ")
print("                 33    9  1 ")
print("                /   ")
print("               54")

print("Con inorder")
T.inorder()
print("L'albero contiene",T.numSx(),"nodi con solo figlio sinistro")
print("\nEseguiamo di nuovo la visita inorder")
T.inorder()
