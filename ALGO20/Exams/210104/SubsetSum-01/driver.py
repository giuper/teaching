from mult import Multi


L=[3,7,6,19,2]
M=[1,1,1,1,2]
T=[9,13,5,10,14,38,25]

print(L)

for t in T:
    s=Multi(L,M,t)
    print(t,"\t",s.Solve())





