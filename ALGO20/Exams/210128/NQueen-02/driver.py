from queen19 import Queen19

for x in range(1,20):
    s=Queen19(x)
    if(s.Solve()):
        print(x)
        print(s)
    else:
        print("No solution found for ",x,"\n")
