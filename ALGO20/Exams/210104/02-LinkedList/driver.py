from SolB import Sol

A=Sol()
A.insertHead(["7 Dicembre 2020",12])
A.insertHead(["6 Dicembre 2020",21])
A.insertHead(["5 Dicembre 2020",2])
A.insertHead(["4 Dicembre 2020",7])
A.insertHead(["3 Dicembre 2020",4])
A.insertHead(["2 Dicembre 2020",3])
A.insertHead(["1 Dicembre 2020",2])

print("Lista input:")
for x in A:
    print(x)

print()
B=A.nuovo()
print("Lista cumulata:")
for x in B:
    print(x)

