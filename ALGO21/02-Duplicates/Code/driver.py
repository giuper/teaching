import time
from zero import DuplicatesS
from uno import Duplicates
SIZE=3*2**11

def driver(theClass):
    print(theClass.desc,"\n\ton an instance of size="+str(SIZE+3))
    start=time.time()
    x=theClass(list(range(SIZE))+[SIZE+10,7,SIZE+20])
    finish=time.time()
    print(f'{"Object creation:":20s}{finish-start:12.4f}')
    
    rep=2
    start=time.time()
    for i in range(rep):
        s1=x[1,SIZE+1]
        s2=x[4,SIZE+3]
    if s1 is None:
        s1=-1
    if s2 is None:
        s2=-1
    finish=time.time()
    print(f'{"Lookup:":20s}{finish-start:12.4f}')
    print(f'{"Average Lookup:":20s}{(finish-start)/(2*rep):12.4f}')
    print(f'{"First result:":29s}{s1:20d}')
    print(f'{"Second result:":29s}{s2:20d}')

if __name__=='__main__':

    classes=[DuplicatesS,Duplicates]
    for cl in classes:
        driver(cl)
        print()
