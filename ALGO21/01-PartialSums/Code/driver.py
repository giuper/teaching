import sys
import time
from zero import parSum
from uno import parSumF
from due import parSumNP
from tre import parSumPre
from quattro import parSumT

def driver(theClass):
    print(theClass.desc,"\n\ton an instance of size="+str(SIZE))
    sys.stdout.flush()
    start=time.time()
    x=theClass(list(range(SIZE)))
    finish=time.time()
    print(f'{"Object creation:":39s}{finish-start:10.6f}')
    
    rep=2
    start=time.time()
    for i in range(rep):
        s1=x[1,SIZE//2]
        s2=x[SIZE//2,SIZE]
    finish=time.time()
    print(f'{"Lookup:":39s}{finish-start:10.6f}')
    print(f'{"Average Lookup:":39s}{(finish-start)/(2*rep):10.6f}')
    print(f'{"First result:":39s}{s1:20d}')
    print(f'{"Second result:":39s}{s2:20d}')
    start=time.time()
    x[SIZE//2-1]=0
    x[SIZE//2+1]=0
    finish=time.time()
    print(f'{"Average Update:":39s}{(finish-start)/(2):10.6f}')
    s1=x[1,SIZE//2]
    s2=x[SIZE//2,SIZE]
    print(f'{"First result after update:":39s}{s1:20d}')
    print(f'{"Second result after update:":39s}{s2:20d}')

if __name__=='__main__':
    SIZE=2**10
    if(SIZE<=2**10):
        classes=[parSum,parSumF,parSumNP,parSumPre,parSumT]
    else:
        classes=[parSumNP,parSumPre,parSumT]

    for cl in classes:
        driver(cl)
        print()
