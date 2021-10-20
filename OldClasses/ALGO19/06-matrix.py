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


class Matrix:

    def __init__(self,nr,nc):
        self._nr=nr
        self._nc=nc
        self._matrix=Array(nr)       
        for i in range(nr):
            self._matrix[i]=Array(nc)

    def __getitem__(self,indices):
        row=indices[0]
        col=indices[1]
        return self._matrix[row][col]

    def __setitem__(self,indices,val):
        row=indices[0]
        col=indices[1]
        self._matrix[row][col]=val


M=Matrix(2,4)
M[1,2]=24
print(M[1,2])
