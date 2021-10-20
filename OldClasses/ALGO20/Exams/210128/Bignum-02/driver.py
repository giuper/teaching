from ltbignum import ltBigNum 

x=ltBigNum("123")
y=ltBigNum("1234")
print(x,"<",y,"\t-->",x<y)

x=ltBigNum("1234")
y=ltBigNum("123")
print(x,"<",y,"\t-->",x<y)

x=ltBigNum("777123")
y=ltBigNum("777124")
print(x,"<",y,"\t-->",x<y)

x=ltBigNum("776124")
y=ltBigNum("776113")
print(x,"<",y,"\t-->",x<y)

for i in range(300,323):
    for j in range(310,343):
        print(i,"<",j,"\t-->",ltBigNum(str(i))<ltBigNum(str(j)))

