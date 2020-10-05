from queen import Queen

for n in range(8,9):
    s=Queen(n)
    if(s.Solve()):
        print(s)
    else:
        print("No solution found for n=",n)

