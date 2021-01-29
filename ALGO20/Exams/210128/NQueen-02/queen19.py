from queen import Queen

class Queen19(Queen):

    def _samecolumn(self,r1,c1,r2,c2):
        if c1!=c2:
            return False
        if c1==c2:
            return abs(r1-r2)<=3
   


