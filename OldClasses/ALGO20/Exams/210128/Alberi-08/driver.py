from lr import tree


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
print(T.lr(),"nodi binari")

T=tree()
T.insert(91,"")
T.insert(77,"L")
T.insert(33,"LR")
T.insert(9,"LL")
T.insert(54,"LLL")
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
print("                 9    33  1 ")
print("                /   ")
print("               54")

print("Con inorder")
T.inorder()
print(T.lr(),"nodi binari")
