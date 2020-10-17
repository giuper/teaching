from maze import Maze

m=Maze(4,5)
for c in range(4):
    m.setBlock(3,c)

for c in range(1,4):
    m.setBlock(0,c)
    m.setBlock(1,c)
m.setFinish(0,3)
#m.setBlock(1,4)
print("Nuovo labirinto")
print(m)

if m.Solve(0,0):
    print("Un cammino")
    #print(m.printSol())
else:
    print("Nessun cammino")
print("\n\n")

