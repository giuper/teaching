from poly import Polynomial
from poly import Monomial

x=Polynomial()
x.append(Monomial(2,1))
x.append(Monomial(3,2))
x.append(Monomial(5,4))
print("polynomial x=\t\t",x)

y=Polynomial()
y.append(Monomial(2,1))
y.append(Monomial(3,2))
y.append(Monomial(4,3))
print("polynomial y:\t\t",y)

z=x+y
print("polynomial z:\t\t",z)

m=Monomial(2,4)
print("monomial m:\t\t",m)
zz=x.mulByMono(m)
print("polynomial zz=x*m:\t",zz)
