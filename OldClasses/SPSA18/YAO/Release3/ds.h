#ifndef _DS

typedef struct {
    int index;
    int type;           /* 0--> input, 1--> intermediate, 2--> output */
    int xIndex;         /* only for input gates*/
    int yIndex;         /* only for input gates*/
    int pGate[2];       /* only for non-input gates */
    int nGate[2];       /* only for non-output gates */
    char *fName;
    int (*funct)(int,int);
    unsigned int gb[2];
    unsigned char *table[2][2];
    unsigned char *keys[2];
} Gate;

#define KEYLEN 16

#define _DS 

#endif

