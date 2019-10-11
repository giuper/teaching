import math


class LineSegment:

#ptA-->(xA,yA)
#ptB-->(xB,yB)
    def __init__(self,ptA,ptB):
        self.A=ptA
        self.B=ptB
        self.xA=ptA[0]
        self.yA=ptA[1]
        self.xB=ptB[0]
        self.yB=ptB[1]
        
    def endPointA(self):
        return self.A
    
    def endPointB(self):
        return self.B
    
    def length(self):
        return math.sqrt((self.xA-self.xB)**2+(self.yA-self.yB)**2)
    
    def isVertical(self):
        return self.xA==self.xB

    def isHorizontal(self):
        return self.yA==self.yB

    def slope(self):
        if self.isVertical():
            return None
        else:
            return (self.yA-self.yB)/(self.xA-self.xB)
        
    def isParallel(self,other):
        return self.slope()==other.slope()

    def isPerpendicular(self,other):
        if self.isVertical():
            return other.isHorizontal()
        if other.isVertical():
            return self.isHorizontal()
        if other.isHorizontal():
            return False
        else:
            return self.slope()==-1/other.slope()
                    


##computes the intersection point of the lines
##of two non-parallel line segments
    def _intersectionPoint(self,other):

#Self (x1,y1)--(x2,y2)
        x1=self.xA
        y1=self.yA
        x2=self.xB  
        y2=self.yB
                    
#Other (t1,z1)--(t2,z2)
        t1=other.xA
        z1=other.yA
        t2=other.xB
        z2=other.yB

#Compute the slope of self and other
        mS=self.slope()
        mO=other.slope()
    
        if(self.isVertical()):
            xStar=x1
            yStar=mO*(x1-t1)+z1

        if(other.isVertical()):
            xStar=t1
            yStar=mS*(t1-x1)+y1

        if(not self.isVertical())and(not other.isVertical()):
#Compute the intercepts
            bS=y1-mS*x1  #y1=mS*x1+bS  same with (x2,y2)
            bO=z1-mO*t1  #z1=mO*t1+bO  same with (t2,z2)

            xStar=-(bS-bO)/(mS-mO)   #abscissa of the intersection
            yStar=xStar*mS+bS
        
        return [xStar,yStar]


    def intersects(self,other):
        x1=self.xA
        x2=self.xB  
        t1=other.xA
        t2=other.xB

##if the line segments are parallel 
        if (self.isParallel(other)):
            if ((x1>=min(t1,t2))and(x1<=max(t1,t2))):
                return True
            if ((x2>=min(t1,t2))and(x2<=max(t1,t2))):
                return True
            return False

        [xStar,yStar]=self._intersectionPoint(other)

        #check if the intersection point belongs to self
        if (xStar>=min(x1,x2)) and (xStar<=max(x1,x2)):
            pass
        else:
            return False

        #check if the intersection point belongs to other
        if (xStar>=min(t1,t2)) and (xStar<=max(t1,t2)):
            pass
        else:
            return False

        return True

    def bisects(self,other):
        if (not self.isPerpendicular(other)):
            return False
        [xStar,yStar]=self._intersectionPoint(other)

        lS1=LineSegment(other.A,[xStar,yStar])
        lS2=LineSegment(other.B,[xStar,yStar])
        return lS1.length()==lS2.length()

    def __str__(self):
        a="("
        a=a+str(self.xA)
        a=a+","
        a=a+str(self.yA)
        a=a+")--("
        a=a+str(self.xB)
        a=a+","
        a=a+str(self.yB)+")"
        return a


