from bigNum2 import bigNum 
from bigNum2 import doubleBigNum 
from bigNum2 import doubleBigNumIterator

x=bigNum("99989")
y=bigNum("2")

xx=iter(x)
yy=iter(y)

print(int(xx.__next__()))
print(int(xx.__next__()))
z=doubleBigNum(x,y)
zzz=doubleBigNumIterator(z)

##for zz in z:
    ##print (int(zz[0]),int(zz[1]))

#z=x+y
#print(z)
#f=x*y
#print(f)
#z=bigNum("2")
#f=f+z
#print(f)
#
#
#y=bigNum("1000")
#x=bigNum("20000")
#f=y*x
#print(x)
#print(y)
#print(f)
