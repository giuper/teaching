from tickerS import TickerS
from tickerS import MaxCapacity

t1=TickerS(5)
for i in range(6):
    try:
        t1.incM()
    except MaxCapacity:
        print("t1: capacita' massima raggiunta")
    else:
        print("t1: incremento effettuato")

print("t1: numero persone",t1.currentP())

t2=TickerS(5)
t2.incF()
print("t2: numero persone",t2.currentP())

print("Sommo i due ticker")
try:
    t3=t1+t2
except MaxCapacity:
    print("t3: capacita' massima raggiunta")
else:
    print("t3: somma effettuata")
    print("t3: numero persone ",t3.currentP())

t1.decM()
t1.decM()
print("t1: numero persone",t1.currentP())

print("Sommo i due ticker")
try:
    t4=t1+t2
except MaxCapacity:
    print("t4: capacita' massima raggiunta")
else:
    print("t4: somma effettuata")
    print("t4: numero persone ",t4.currentP())

