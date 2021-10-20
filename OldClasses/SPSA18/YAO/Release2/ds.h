#ifndef _DS

typedef struct {
    int index;
    int type;     /* 0--> input, 1--> intermediate, 2--> output */
    int xIndex;   /* only for input gates*/
    int yIndex;   /* only for input gates*/
    int pGate[2]; /* only for non-input gates */
    int nGate[2]; /* only for non-output gates */
    char *fName;
    int (*funct)(int,int);
    unsigned int gb[2];
    int table[2][2];
    unsigned int keys[2];
} Gate;

#define _DS 

#endif

