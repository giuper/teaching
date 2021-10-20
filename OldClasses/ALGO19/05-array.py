import ctypes

class Array:

    def __init__(self,size):
    
        assert size>0,"Array size must be positive"
        self._size=size
        arrType=ctypes.py_object*size
        self._arr=arrType()
        self.clear(None)

    def __len__(self):
        return self._size

    def __setitem__(self,ind,val):
        assert ind>=0 and ind<self._size,"Invalid index"
        self._arr[ind]=val

    def __getitem__(self,ind):
        assert ind>=0 and ind<self._size,"Invalid index"
        return self._arr[ind]


    def __iter__(self):
        return _ArrayIterator(self._arr)

    def clear(self,vr):
        for i in range(self._size):
            self._arr[i]=vr

class _ArrayIterator:

    def __init__(self,theArr):
        self._arr=theArr
        self._cur=0

    def __iter__(self):
        return self

    def __next__(self):
        if self._cur<len(self._arr):
            item=self._arr[self._cur]
            self._cur+=1
            return item
        else:
            raise StopIteration




l=10
##solo come esempio di
##try annidati
##da non usare in codice vero 

try:
    A=Array(l)
except AssertionError as err:
    try:
        A=Array(-l)
    except AssertionError as err:
        A=Array(1)
    
print(len(A))
A[2]='Pippo'
print(A[2])
A[3]=A[2]
print(A[3])

for i in range(len(A)):
    A[i]=i

for x in A:
    print(x)
A.clear('Pluto')
for x in A:
    print(x)
