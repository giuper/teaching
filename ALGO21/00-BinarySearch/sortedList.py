from binarySearch import BSRec

class SortedList(list):

    def __contains__(self,x):
        idx=BSRec(self,x)
        return idx!=len(self) and self[idx]==x


