from binarySearch import BSRec

##SortedList is a class derived from list
##we override __contains__ so that the in construct
##executes binary search

class SortedList(list):

    def __contains__(self,x):
        idx=BSRec(self,x)
        return idx!=len(self) and self[idx]==x


