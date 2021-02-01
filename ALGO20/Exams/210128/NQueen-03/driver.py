from queen19 import Queen19

for n in range(1,20):
    for d in range(1,n):
        s=Queen19(n,d)
        if(s.Solve()):
            print("Soluzione trovata per",n,d)
        else:
            print("Nessuna soluzione trovata per",n,d)
