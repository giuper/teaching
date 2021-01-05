from eqbignum import eqbigNum 

x=eqbigNum("123")
y=eqbigNum("123")
print(x,y,"\t-->",x==y)
y=eqbigNum("1923")
print(x,y,"\t-->",x==y)
y=eqbigNum("1239")
print(x,y,"\t-->",x==y)
x=eqbigNum("1234567890")
y=eqbigNum("12345678901")
print(x,y,"\t-->",x==y)
print(x,y,"\t-->",y==x)
y=eqbigNum("1234567890")
print(x,y,"\t-->",x==y)
print(x,x,"\t-->",x==x)
print(y,y,"\t-->",y==y)


