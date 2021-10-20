#include "ds.h"

/* simple decoding
   only works for 3-gate circuits
*/

int
decodeS(Gate *circuit,int *y)
{

    Gate *input0=circuit;
    Gate *input1=circuit+1;
    Gate *output=circuit+2;

    int y0=y[input0->yIndex];
    int K0=input0->table[y0][0];
    int ROW=input0->table[y0][1];

    int y1=y[input1->yIndex];
    int K1=input1->table[y1][0];
    int COL=input1->table[y1][1];

    return K0^K1^output->table[ROW][COL];
}
