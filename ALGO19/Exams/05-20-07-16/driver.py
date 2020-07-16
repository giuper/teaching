from sol import sol

for i in range(3,21):
    q=sol(i,[[0,0]]) #la casella [0,0] e' l'unica casella proibita
    if q.solve():
        print(i)
        print(q)
        print()
    else:
        print(i,": nessuna sol.")
        print()


