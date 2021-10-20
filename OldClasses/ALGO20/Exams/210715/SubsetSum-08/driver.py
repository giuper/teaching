from pm12 import PM12


L=[4,8,6,10]

print(L)

for t in range(1,sum(L)+1):
    s=PM12(L,t)
    print("t=",t)
    if s.Solve():
        print(s)
    else:
        print("Input:\t",L)
        print("No sol")
    print()


