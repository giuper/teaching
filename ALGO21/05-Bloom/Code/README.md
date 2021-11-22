# ALGO21: *Algoritmi e Strutture Dati* #
## Corso di Laurea Triennale in *Statistica per i Big Data* ##
### Anno Accademico 2021/22 ###

Prof. [Giuseppe Persiano](https://giuper.github.io)


## Bloom filter ##

Il file [Bloom.py](./Bloom.py) presenta una semplice implementazione
di un filtro di Bloom.

0.  La funzione  ```esempioSemplice``` crea un Bloom filter di taglia 20 
    con 2 hash function ed inserisce alcuni personaggi del mondo Disney.

1. La funzione ```falsiPositiviK(M,N)``` mostra come varia
il numero di falsi positivi come funzione del numero k di funzioni hash.
I valori scelti sono vicini all'ottimo teorico M/N*ln(2)


2. La funzione ```falsiPositiviL(M)``` mostra come
varia il numero di falsi positivi come funzione del carico L=M/N del filtro
quando il numero di funzioni hash usate &egrave; uguale all'ottimo
M/N*ln(2)

    Questo [file](FalsePositiveAtOptimum.txt) riporta l'output di questa
    funzione. I valori relativi ai tempi di esecuzione non sono tutti
    significativi.
