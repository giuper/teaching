# ALGO20: *Algoritmi e Strutture Dati* #
## Corso di Laurea Triennale in *Statistica per i Big Data* ##
### Anno Accademico 2020/21 ###


## Algoritmi di Backtrack per Subset Sum ##
Tutte le classi sono derivate da [una classe generale per backtrack](back.py) che utilizza la struttura dati [stack](stack.py)

1. Primo algoritmo.

    Sono provate tutte le mosse e uno stato è considerato finale solo
    se abbiamo una decisione su tutti gli elementi

    [file con la classe](subsetSum0.py)

    [file che richiama la classe](ds0.py)

    [output file](aaa0)

    Tempo di esecuzione sul mio portatile 134s
   
2. Secondo algoritmo.

    Un elemento non &grave; aggiunto se mi farebbe eccedere il target
    se abbiamo una decisione su tutti gli elementi

    [file con la classe](subsetSum1.py)

    [file che richiama la classe](ds1.py)

    [output file](aaa1)
   
    Tempo di esecuzione sul mio portatile 88s

3. Terzo algoritmo.

    Non scarta un elemento che mi porta in uno stato in cui, anche aggiungendo 
    tutti gli altri rimanenti, mi troverei sotto il target, 

    [file con la classe](subsetSum2.py)

    [file che richiama la classe](ds2.py)

    [output file](aaa2)
   
    Tempo di esecuzione sul mio portatile 14s

3. Quarto algoritmo.
    
    Risolve due piccole inefficienze del terzo algoritmo

    [file con la classe](subsetSum4.py)

    [file che richiama la classe](ds4.py)

    [output file](aaa4)
   
    Tempo di esecuzione sul mio portatile 11s

4. Soluzione per l'assegno

    In questa versione del problema non &grave; possibile mettere in soluzione due interi che appaiono in posizioni consecutive nella lista L 

    [file con la classe](subsetSum5.py)

    [file che richiama la classe](ds5.py)
