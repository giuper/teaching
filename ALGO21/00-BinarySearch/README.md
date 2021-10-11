# ALGO21: *Algoritmi e Strutture Dati* #
## Corso di Laurea Triennale in *Statistica per i Big Data* ##
### Anno Accademico 2021/22 ###

Prof. [Giuseppe Persiano](https://giuper.github.io)

### Binary Search ###

0. [binarySearch.py](./binarySearch.py)
    contains the implementation of 4 search algorithms on sorted lists

    0. the *in* python construct (*inP* function)
    1. the *linear search* algorithm (*LS* function)
    2. the *iterative binary search* algorithm (*BSIter*)
    3. the *recursive binary search* algorithm (*BSRec*)

    
    The function *driverS* invokes all four implementations
    on lists of increasing length and measures the time
    taken


| Algorithm |  Size | Time|
| ---       | ---:  | ---:|
| Python in           |       512   |        0.000013 | 
| Linear search       |       512   |        0.000074 | 
| Bin Search Iter     |       512   |        0.000009 | 
| Bin Search Rec      |       512   |        0.000013 | 
|                     |             |                 | 
| Python in           |      2048   |        0.000046 | 
| Linear search       |      2048   |        0.000255 | 
| Bin Search Iter     |      2048   |        0.000009 | 
| Bin Search Rec      |      2048   |        0.000013 | 
|                     |             |                 | 
| Python in           |     16384   |        0.000343 | 
| Linear search       |     16384   |        0.001918 | 
| Bin Search Iter     |     16384   |        0.000012 | 
| Bin Search Rec      |     16384   |        0.000019 | 
|                     |             |                 | 
| Python in           |    131072   |        0.002733 | 
| Linear search       |    131072   |        0.014796 | 
| Bin Search Iter     |    131072   |        0.000014 | 
| Bin Search Rec      |    131072   |        0.000017 | 
|                     |             |                 | 
| Python in           |    524288   |        0.005170 | 
| Linear search       |    524288   |        0.025377 | 
| Bin Search Iter     |    524288   |        0.000008 | 
| Bin Search Rec      |    524288   |        0.000009 | 
|                     |             |                 | 
| Python in           |   2097152   |        0.019714 | 
| Linear search       |   2097152   |        0.100176 | 
| Bin Search Iter     |   2097152   |        0.000010 | 
| Bin Search Rec      |   2097152   |        0.000011 | 
|                     |             |                 | 
| Python in           |  16777216   |        0.156145 | 
| Linear search       |  16777216   |        0.823720 | 
| Bin Search Iter     |  16777216   |        0.000012 | 
| Bin Search Rec      |  16777216   |        0.000012 | 
|                     |             |                 | 
| Python in           | 134217728   |        1.300149 | 
| Linear search       | 134217728   |        6.267402 | 
| Bin Search Iter     | 134217728   |        0.000014 | 
| Bin Search Rec      | 134217728   |        0.000013 | 


1. Class [SortedList](sortedList.py) overrides the 
    *__contains__* method of the class *list*. 
    In file [driverInt.py](driverInt.py) we execute *in* 
    for lists and sorted lists of varying size.
    For lists of size 134217728, sorted lists have a speedup of
    40000-50000x circa.

### Select ###
The python implementations for the algorithms for Select are found in [this](./SelectImpl) folder.

1. [Deterministic Recursive Select](./SelectImpl/DetRecSelect.py) vs 
   [Randomized Recursive Select](./SelectImpl/RandRecSelect.py)

    We run the deterministic and randomized select algorithms
    implemented using recursion on the worst case (ordered list).
    The deterministic algorithm stops working for lists 
    of around 1000 elements (for exceeding maximum recursion depth).
    The randomized algorithm works up to lists of 200 Million elements
    (and then stops for lack of space).
    See [Battle of Recursive](BattleRecSelective.py).

        
2. [Deterministic Iterative Select](./SelectImpl/DetIteSelect.py) vs 
   [Randomized Iterative Select](./SelectImpl/RandIteSelect.py)

    We run the deterministic and randomized select algorithms
    implemented using iteration on the worst case (ordered list).
    See [Battle of Iterative](BattleIteSelective.py).

    The iterative algorithms use the [partition](./SelectImpl/Partition.py)
    function described in [these](Notes/partition.pdf) notes.
        


### Exercises ###

Exercises are found in [this](./Esercizi.md) (in Italian)
