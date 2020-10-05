from maze import Maze

m=Maze(4,5,0,0)  #specify dimensions and starting point

#throw in some blocks
for c in range(4):
    m.setBlock(3,c)
for c in range(1,4):
    m.setBlock(0,c)
    m.setBlock(1,c)

#set the finish goal
m.setFinish(0,3)

#uncomment the following to get a maze with no solution
#m.setBlock(1,4)  
print("Labirinto")
print()
print(m)

if m.Solve():
    print("Cammino trovato")
    print(m)
else:
    print("Nessun cammino trovato")
print("\n\n")

