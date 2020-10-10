from queen import Queen

for x in range(1,20):
    s=Queen(x)
    if(s.Solve()):
        print(x)
        print(s)
    else:
        print("No solution found for ",x,"\n")

