
### Esercizi su ricerca binaria e select ###

1. Una lista *A* di *N* elementi distinti è *bitonica*  se esiste un indice *j* tale che

    1. per *0<= i<j*, abbiamo che  *A[i]<A[i+1]*

    2. per *j<= i<N-1*, abbiamo che *A[i]>A[i+1]*

    In altre parole, la sottolista *A[0:j+1]* è crescente e la 
    sottolista *A[j:N]* è decrescente e quindi il massimo è *A[j]*.

    Progettare ed implementare in python un algoritmo che resituisce il
    valore massimo di una lista bitonica in tempo *O(log N)*

2. Modificare gli algoritmi per il problema *Select* in modo da ottenere
        in output tutti i primi *k* elementi più piccoli della lista input.

3. Il problema *DoubleSelect(A,k)* chiede  di calcolare il *k*-esimo elemento più grande e il *k*-esimo elemento più piccolo.

