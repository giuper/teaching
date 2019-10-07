from LineSegment import LineSegment 

def stampa(P,P1):
    if (P.intersects(P1)):
        print(P," intersects ",P1)
    else:
        print(P," does not intersect ",P1)


P =LineSegment([1.0,1.0],[3.0,3.0])

P1=LineSegment([2.0,1.0],[1.0,2.0])
P2=LineSegment([2.0,3.0],[1.0,3.0])
P3=LineSegment([4.0,2.0],[2.0,4.0])
P4=LineSegment([5.0,3.0],[8.0,0.0])
P5=LineSegment([3.0,3.0],[3.0,2.0])
P6=LineSegment([3.0,3.0],[4.0,3.0])
P7=LineSegment([3.1,3.0],[4.0,3.0])
P8=LineSegment([4.0,0.0],[4.0,7.0])

stampa(P,P1)
stampa(P,P2)
stampa(P,P3)
stampa(P,P4)
stampa(P,P5)
stampa(P,P6)
stampa(P,P7)
stampa(P,P8)

print(" ")

P =LineSegment([1.0,3.0],[3.0,3.0])
stampa(P,P1)
stampa(P,P2)
stampa(P,P3)
stampa(P,P4)
stampa(P,P5)
stampa(P,P6)
stampa(P,P7)
stampa(P,P8)


P=LineSegment([1.0,0.0],[0.0,1.0])
A=LineSegment([0.0,0.0],[2.0,2.0])

if(P.bisects(A)):
    print(P," bisects ",A)
else:
    print(P," does not bisect ",A)

if(A.bisects(P)):
    print(A," bisects ",P)
else:
    print(A," does not bisect ",P)







