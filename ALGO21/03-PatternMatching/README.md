# ALGO21: *Algoritmi e Strutture Dati* #
## Corso di Laurea Triennale in *Statistica per i Big Data* ##
### Anno Accademico 2021/22 ###

Prof. [Giuseppe Persiano](https://giuper.github.io)


## Pattern Matching ##

0. Algoritmo di Forza Bruta 
1. Algoritmo di Knuth-Morris-Pratt
2. Algoritmo di Rabin-Karp


[Slide](./Slides/pm.pdf) disponibili 

Per algoritmo di Rabin-Karp, Capitolo 2.3.3 di 
*Algorithms and Data Structures for Massive Datasets*
di Medjedovic e Tahirovic.

[Codice](./Code)


## Esercizi ##

1. Pattern Matching Parziale. Modifica l'algoritmo di forza bruta in modo da individuare tutte i valori s tali che il pattern P e il testo T[s:s+m] differiscono in al più una posizione.
2. Pattern Matching con Alternative. In pattern matching tradizionale il pattern è una stringa, cioè una lista di caratteri. Consideriamo invece un pattern esteso come una lista di liste di caratteri. Ad esempio, il pattern esteso P=['a','b',['c','d']] ha match sia con la stringa 'abc' che con la stringa 'abd'. Quindi il testo 'ababcaabdaa' contiene occorrenze del pattern per s=2,6. L'esercizio richiede di modificare l'algorito di forza bruta per il pattern matching in modo da individuare anche occorrenze di pattern estesi all'interno di un testo.
