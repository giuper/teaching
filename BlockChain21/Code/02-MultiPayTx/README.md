# ALGO21: *Algoritmi e Strutture Dati* #
## Corso di Laurea Triennale in *Statistica per i Big Data* ##
### Anno Accademico 2021/22 ###

## Partial Sums ##

A data structure that supports the following two operations:

1. *Init* that takes a list *A* of *n* elements
2. *Lookup* that takes two integers *0  ≤ i < j  ≤n* and returns
    the sum of all elements from *A[i]* to *A[j-1]*

The dynamic version includes a third operation *Set* that takes 
integer *k* and value *val* and sets *A[k]=val*


We will implement the data structure as a python class.
The *Init* operation is the class constructor *__init__*;
the *Lookup* operation is implemented by the *__getitem__* operation
and can thus be invoked by *A[i,j]*;
the *Set* operation is implemented by the *__setitem__* operation and
can thus be invoked by *A[k]=val*.



### First algorithm: Precompute and store all answers ##

1.  We precompute and store all the possible answers
in a two-dimensional list *A[i][j]*;
    1. Memory: *O(n^2)*
    2. Time for *Init*: *O(n^2)* 
2. *Lookup(i,j)* is implemented by returning *A[i][j]*;
    1.  Time for *Lookup*: *O(1)* 
3. *Set(k,val)* is implemented by modifying all *A[i][j]* with *i ≤ k < j*
    1. Time for *Set*: *O(n^2)* 


Code available [here](./Code/zero.py)

Also, see [here](./Code/uno.py) for faster precomputation


### Second algorithm: No Precomputation ##

1.  We store input list *A*
    1. Memory: *O(n)*
    2. Time for *Init*: *O(n)*
2. *Lookup(i,j)* is implemented by summing all elements of *A* from *A[i]* 
    to *A[j-1]*
    1. Time for *Lookup*: *O(n)*
3. *Set(k,val)* is implemented by modifying all *A[k]* 
    1. Time for *Set*: *O(1)* 

Code available [here](./Code/due.py)

### Third algorithm: Precompute prefixes ##

1. We compute *Prefixes[k]=A[0]+A[1]+...+A[k-1]*, for *k=0,...,N+1*
    1. Memory: *O(n)*
    2. Time for *Init*: *O(n)*
2. *Lookup(i,j)* is computed by returning *Prefixes[j]-Prefixes[i]*
    1. Time for *Lookup*: *O(1)*
3. *Set(k,val)* is implemented by modifying *Prefixes[i]*, for *i=k+1,...,N+1* 
    1. Time for *Set*: *O(n)* 
   
Code available [here](./Code/tre.py)

### Fourth algorithm: The tree ##

Code available [here](./Code/quattro.py)
(See [slides](Slides/partialSum.pdf))


### Evaluating the algorithms ##

Code available [here](./Code/driver.py)

### Esercizi ###

1. Modificare le implementazioni per il minimo (o il massimo) di un intervallo. Nota che non tutti gli algoritmi discussi possono essere modificati. Perché?
2. Modificare il codice in modo che funzioni per tutte le operazioni associative con un elemento neutro. 
3. Spiegare perché l'implementazione di [uno.py](./uno.py) riesce ad effettuare la __init__ più velocemente di [zero.py](./zero.py)
