from DUE import DUE


LP=[4,12]
LM=[1,3]

for x in range(1,sum(LP)+1):
    s=DUE(LP,LM,x)
    if s.Solve():
        print(x,"ha soluzione")
    else:
        print(x,"non ha soluzione")

