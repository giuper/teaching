# ALGO20: *Algoritmi e Strutture Dati* #
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



### First algorithm ###
We precompute and store all the possible answers
in a two-dimensional list *A[i][j]*;
*Lookup(i,j)* is implemented by returning *A[i][j]*;
*Set(k,val)* is implemented by modifying all *A[i][j]* with *i ≤ k < j*


1. Memory: *O(n^2)*
2. Time for *Init*: *O(n^2)* 
3. Time for *Lookup*: *O(1)* 
4. Time for *Set*: *O(n^2)* 


