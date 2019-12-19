from gc import nReginePacMan
#sostituire pacMan con il nome del file specificato dalla traccia

def exam(a,b):
    solution=[]
    for i in range(a,b):
        q=nReginePacMan(i)
        if q.hasSolution():
            solution.append(i)
    return solution



print(exam(4,15))
            
