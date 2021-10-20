from SBST import SBST

print("Primo test")
X=SBST()
for i in range(10,20):
    #j=10-i
    #k=i+10
    X.insert(i,i*i)
    #X.insert(j,j*j)
    #X.insert(k,k*k)

print("Visita inorder")
X.inorder()
print("minimo",X.min())
print("massimo",X.max())
print("secondo minimo",X.smin())


print("\nSecondo test")
X=SBST()
for i in range(10,20):
    j=10-i
    X.insert(j,j*j)

print("Visita inorder")
X.inorder()
print("minimo",X.min())
print("massimo",X.max())
print("secondo minimo",X.smin())

print("\nTerzo test")
X=SBST()
for i in range(10,20):
    j=i-10
    k=i+10
    X.insert(i,i*i)
    X.insert(j,j*j)
    X.insert(k,k*k)

print("Visita inorder")
X.inorder()
print("minimo",X.min())
print("massimo",X.max())
print("secondo minimo",X.smin())




