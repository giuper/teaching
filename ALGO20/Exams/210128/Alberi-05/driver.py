from listpari import tree


T=tree()
T.insert(91,"")
T.insert(77,"L")
T.insert(33,"LL")
T.insert(54,"LLR")
T.insert(9,"LR")
T.insert(6,"R")
T.insert(1,"RL")
T.insert(5,"RR")

print("Albero: ")


print("                       91 ")
print("                      /  \ ")
print("                     /    \ ")
print("                    77     6")
print("                   / \    / \ ")
print("                  /   \   | | ")
print("                 33    9  1 5")
print("                  \ ")
print("                   54")

print("Con inorder")
T.inorder()

print(T.listaPari(),"nodi contenenti interi pari")
print("\nEseguiamo di nuovo la visita inorder")
T.inorder()

T=tree()
T.insert(90,"")
T.insert(77,"L")
T.insert(33,"LL")
T.insert(54,"LLL")
T.insert(94,"LR")
T.insert(3,"R")
T.insert(2,"RL")

print()
print()
print("Albero: ")


print("                       90 ")
print("                      /  \ ")
print("                     /    \ ")
print("                    77     3")
print("                   / \    / ")
print("                  /   \   |  ")
print("                 33   94  2 ")
print("                /   ")
print("               54")

print("Con inorder")
T.inorder()
print(T.listaPari(),"nodi contenenti interi pari")
print("\nEseguiamo di nuovo la visita inorder")
T.inorder()
