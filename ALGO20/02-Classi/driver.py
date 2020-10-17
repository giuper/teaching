from ticker import Ticker

#esempio di utilizzo della classe Ticker

t1=Ticker()
print(t1.current())
t1.inc()
t1.inc()
print(t1.current())
t1.inc()
print(t1.current())
t1.dec()
print(t1.current())

t2=Ticker()
print(t2.current())

A=[]
for i in range(4):
    A.append(Ticker())

A[2].inc()
print("Stampo il numero di persone dei ticker nella lista A")
for i in range(4):
    print(i,"\t",A[i].current())
    
