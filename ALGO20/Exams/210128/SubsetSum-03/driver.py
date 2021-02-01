from pm import PM


L=[3,7,6,19,2]

print(L)

for t in range(1,38):
    s=PM(L,t)
    print("t=",t)
    if s.Solve():
        print(s)
    else:
        print("Input:\t",L)
        print("No sol")
    print()


