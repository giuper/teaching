from LineSegment import LineSegment 

##Caso 1.a Segmenti verticali su rette differenti
S=LineSegment([3.0,1.0],[3.0,3.0])
O=LineSegment([4.0,1.0],[4.0,3.0])
assert not S.intersects(O), "Errore per segmenti verticali su rette differenti"
assert not O.intersects(S), "Errore per segmenti verticali su rette differenti"


##Caso 1.b Segmenti verticali su rette coincidenti
S=LineSegment([3.0,1.0],[3.0,3.0])
O=LineSegment([3.0,1.5],[3.0,3.4])
assert S.intersects(O), "Errore per segmenti verticali sulla stessa retta"
assert O.intersects(S), "Errore per segmenti verticali sulla stessa retta"


##Case 2.a Segmenti paralleli e non verticali su rette differenti
S=LineSegment([3.0,1.0],[3.0,3.0])
O=LineSegment([3.0,4.0],[3.0,7.0])
assert not S.intersects(O), "Errore per segmenti paralleli su rette differenti"
assert not O.intersects(S), "Errore per segmenti paralleli su rette differenti"

##Case 2.b Segmenti paralleli e non verticali su rette coincidenti
S=LineSegment([0.0,0.0],[3.0,3.0])
O=LineSegment([4.0,4.0],[5.0,5.0])
assert not S.intersects(O), "Errore per segmenti paralleli sulla stessa retta"
assert not O.intersects(S), "Errore per segmenti paralleli sulla stessa retta"

S=LineSegment([0.0,0.0],[3.0,3.0])
O=LineSegment([1.0,1.0],[2.0,2.0])
assert S.intersects(O), "Errore per segmenti paralleli sulla stessa retta"
assert O.intersects(S), "Errore per segmenti paralleli sulla stessa retta"

S=LineSegment([0.0,0.0],[3.0,3.0])
O=LineSegment([1.0,1.0],[5.0,5.0])
assert S.intersects(O), "Errore per segmenti paralleli sulla stessa retta"
assert O.intersects(S), "Errore per segmenti paralleli sulla stessa retta"

S=LineSegment([0.0,2.0],[3.0,5.0])
O=LineSegment([1.0,3.0],[5.0,7.0])
assert S.intersects(O), "Errore per segmenti paralleli sulla stessa retta"
assert O.intersects(S), "Errore per segmenti paralleli sulla stessa retta"

##Case 3 Segmenti non paralleli
S=LineSegment([0.0,2.0],[3.0,5.0])
O=LineSegment([1.0,0.0],[1.0,7.0])
assert S.intersects(O), "Errore per segmenti non paralleli e uno verticale"
assert O.intersects(S), "Errore per segmenti non paralleli e uno verticale"

S=LineSegment([0.0,8.0],[3.0,11.0])
O=LineSegment([1.0,0.0],[1.0,7.0])
assert not S.intersects(O), "Errore per segmenti non paralleli e uno verticale"
assert not O.intersects(S), "Errore per segmenti non paralleli e uno verticale"

S=LineSegment([0.0,0.0],[3.0,5.0])
O=LineSegment([1.0,0.0],[0.0,1.0])
assert S.intersects(O), "Errore per segmenti non paralleli e non verticali"
assert O.intersects(S), "Errore per segmenti non paralleli e non verticali"

