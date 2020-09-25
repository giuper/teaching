from tickerS import TickerS

t1=TickerS()
t1.incM()
t1.incF()
t1.incF()

t2=TickerS()
t2.incM()
t2.incM()
t2.incM()
t2.incF()
#creo un oggetto della classe tickerS
#che e' la "somma" dei due ticker

t=t1+t2

print("Numero M nel nuovo oggetto: \t",t.currentM())
print("Numero F nel nuovo oggetto: \t",t.currentF())
