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
                    

##returns True if point belongs to segment self
    def _isPointOn(self,point):
        [x,y]=point

        if (self.isVertical()):
            [y1,y2]=[min(self.yA,self.yB),max(self.yA,self.yB)]
            return (y>=y1) and (y<=y2)
        else:
            [x1,x2]=[min(self.xA,self.xB),max(self.xA,self.xB)]
            return (x>=x1) and (x<=x2)

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

    
#Both are vertical
        if (self.isVertical() and other.isVertical()):
            if x1!=t1: #Vertical but not on the same line
                return False
#Vertical on the same line
            [y1,y2]=[min(self.yA,self.yB),max(self.yA,self.yB)]
            [z1,z2]=[min(other.yA,other.yB),max(other.yA,other.yB)]
            if (y2<z1) or (z2<y1):
                return False
            else:
                return True

##Parallel and neither is vertical
        if (self.isParallel(other)):
            mS=self.slope()
            mO=other.slope()
            bS=self.yA-mS*x1  
            bO=other.yA-mO*t1 
##Parallel distinct lines
            if (bS!=bO):
                return False
##On the same non-vertical line
            else:
                [x1,x2]=[min(self.xA,self.xB),max(self.xA,self.xB)]
                [t1,t2]=[min(other.xA,other.xB),max(other.xA,other.xB)]
                if (x2<t1) or (t2<x1):
                    return False
                else:
                    return True

##Non-parallel  (one might be vertical)
        [xStar,yStar]=self._intersectionPoint(other)

        return self._isPointOn([xStar,yStar]) and other._isPointOn([xStar,yStar]) 

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


