import time
from sortedList import SortedList

def driverInt(sizes):

    print("Sorted List ")
    for size in sizes:
        L=SortedList(list(range(0,size,2)))
        start=time.time()
        x=0 in L
        y=1 in L
        z=size+1 in L
        finish=time.time()
        print(f'{"Size:":7s}{(size//2):10d}{"  Average time:":20s}{(finish-start)/3:10.6f}')

    sortedT=finish-start
    print()

    print("Python List ")
    for size in sizes:
        L=list(range(0,size,2))
        start=time.time()
        x1=0 in L
        y1=1 in L
        z1=size+1 in L
        finish=time.time()
        print(f'{"Size:":7s}{(size//2):10d}{"  Average time:":20s}{(finish-start)/3:10.6f}')
    pythonT=finish-start

    print()
    print(f'{"Speedup":12s}{pythonT/sortedT:10.6f}')

if __name__=='__main__':
    sizes=[2**10,2**12,2**15,2**18,2**20,2**22,2**25,2**28]
    driverInt(sizes)

