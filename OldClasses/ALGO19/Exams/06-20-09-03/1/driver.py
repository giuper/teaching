from soldp import soldp

print("Risolviamo il problema partendo da configurazioni iniziali senza alcuna regina, per n=3,...,9")
print()

for n in range(3,10):
    q=soldp(n,[-1]*n) #la configurazione iniziale non contiene alcuna regina
    print(n)
    if q.solve():
        print("Ho trovato una soluzione")
        print(q)
        print()
    else:
        print("Non ho trovato nessuna soluzione")
        print()


print("Risolviamo il problema per n=4, per tutte le possibili posizioni di una regina sulla prima riga")
print ()
for x in range(4):
    print ("x=",x)
    q=soldp(4,[x,-1,-1,-1])
    if q.solve():
        print("Ho trovato una soluzione")
        print(q)
        print()
    else:
        print("Non ho trovato nessuna soluzione")
        print()

