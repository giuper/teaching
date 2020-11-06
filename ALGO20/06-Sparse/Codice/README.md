# ALGO20: *Algoritmi e Strutture Dati* #
## Corso di Laurea Triennale in *Statistica per i Big Data* ##
### Anno Accademico 2020/21 ###


## Binary Search ##
Implementazioni della struttura dati astratta Sparse Matrix

1. Lista non ordinata

    Gli elementi non-zero della matrice sono in una lista non ordinata e 
    dobbiamo cercare l'intera classe per verificare se un elemento è presente.

    [file con la classe](sparseMatrix.py)

2. Lista ordinata

    Gli elementi non-zero della matrice sono in una lista ordinata e 
    usiamo la ricerca binaria per verificare se un elemento è presente.
    

    [file con la classe sviluppata a lezione](sparseMatrixLezione.py)

    [file con la classe ripulita](sparseMatrixBS.py)


In questo [file] (driver.py) confronto i tempi delle due classi su matrici sparse
di dimensioni medie. I risultati di un'esecuzione sul mio portatile si trovano
in questo [file](result.txt). Notate lo speed-up offerto dalla ricerca binaria!!!

