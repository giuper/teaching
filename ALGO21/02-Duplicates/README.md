# ALGO20: *Algoritmi e Strutture Dati* #
## Corso di Laurea Triennale in *Statistica per i Big Data* ##
### Anno Accademico 2021/22 ###


## Duplicates in a range ##

A data structure that supports the following two operations:

1. *Init* that takes a list *A* of *n* elements
2. *Lookup* that takes two integers *0  ≤ i < j  ≤n* and it checks
    if there is a duplicate element in the interval from
    *A[i]* to *A[j-1]*.
    If such a duplicate exists the algorithm returns the duplicate element.

We will implement the data structure as a python class.
The *Init* operation is the class constructor *__init__*;
the *Lookup* operation is implemented by the *__getitem__* operation
and can thus be invoked by *A[i,j]*.



### Algorithm: Precompute and store all answers ###

1.  We precompute and store all the possible answers
in a two-dimensional list *A[i][j]*;
    1. Memory: *O(n^2)*
    2. Time for *Init*: *O(n^2)* 
2. *Lookup(i,j)* is implemented by returning *A[i][j]*;
    1.  Time for *Lookup*: *O(1)* 


Code available [here](./Code/zero.py)


### Algorithm: A Faster Algorithm ###

1. For each *i* compute the following two quantities
    1. *P[i]* that is set to the largest *j<i* such that *A[j]=A[i]*.
        If no such  *j* exists *P[i]=-1*
        1. Memory and time *O(n)*
    2. *Q[i]* the largest value of *P[j]* for *j<= i*
        1. Memory and time *O(n)*
    
    
2.  *Lookup(i,j)* is implemented by checking if *Q[j-1]<i*.
        If this the case then no there is no duplicate in *[i,j)*.
        Otherwise, *A[Q[j-1]]* is a duplicate.
    1. Time *O(1)*

Code available [here](./Code/uno.py)

