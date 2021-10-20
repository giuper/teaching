from queen import Queen

class Queen19(Queen):

    def _tooclose(self,r1,c1,r2,c2):
        return abs(r1-r2)==1 and abs(c1-c2)<=2
   
    ##check if queen in (r1,c1) attacks queen in (r2,c2)
    def _attackingQ(self,r1,c1,r2,c2):
        return self._tooclose(r1,c1,r2,c2) or self._samecolumn(r1,c1,r2,c2) or self._sameMajorD(r1,c1,r2,c2) or self._sameMinorD(r1,c1,r2,c2)



