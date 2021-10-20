#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <openssl/conf.h>
#include <openssl/evp.h>
#include <openssl/err.h>
#include <openssl/rand.h>

#include "ds.h"
#include "templates.h"


void
printKey(unsigned char *key, int len, FILE *fd){

    int i;
    for(i=0;i<len;i++)
        fprintf(fd,"%d ",(unsigned int) key[i]);
    fprintf(fd,"\n");

}

void
writeOutputGate(Gate *gate, FILE *fd)
{

        fprintf(fd,"%d %d\n",gate->pGate[0],gate->pGate[1]);
        fprintf(fd,"%s\n",gate->fName);
        printKey(gate->table[0][0],KEYLEN,fd);
        printKey(gate->table[0][1],KEYLEN,fd);
        printKey(gate->table[1][0],KEYLEN,fd);
        printKey(gate->table[1][1],KEYLEN,fd);
        fprintf(fd,"\n");
}

void
writeIntermediateGate(Gate *gate, FILE *fd)
{

        fprintf(fd,"%d %d\n",gate->pGate[0],gate->pGate[1]);
        fprintf(fd,"%d %d\n",gate->nGate[0],gate->nGate[1]);
        fprintf(fd,"%s\n",gate->fName);
        printKey(gate->table[0][0],2*KEYLEN,fd);
        printKey(gate->table[0][1],2*KEYLEN,fd);
        printKey(gate->table[1][0],2*KEYLEN,fd);
        printKey(gate->table[1][1],2*KEYLEN,fd);
        fprintf(fd,"\n");
}

void
writeInputGate(Gate *gate, FILE *fd)
{
        fprintf(fd,"%d\n",gate->yIndex);
        fprintf(fd,"%d %d\n",gate->nGate[0],gate->nGate[1]);
        fprintf(fd,"%s\n",gate->fName);
        printKey(gate->table[0][0],KEYLEN,fd);
        fprintf(fd,"%d\n",*(gate->table[0][1]));
        fprintf(fd,"\n");
}


void
selectGarb(Gate *circuit, int *y, int numOfGates)
{

    int i,s;
    Gate *current;

    for(i=0;i<numOfGates;i++){
        current=circuit+i;
        if(current->type!=0)
            continue;

/* it is an input gate */
        s=y[current->yIndex];
        free(current->table[1-s][0]);
        free(current->table[1-s][1]);
        current->table[0][0]=current->table[s][0];
        current->table[0][1]=current->table[s][1];
        current->table[1][0]=NULL;
        current->table[1][1]=NULL;
    }
}

void
writeGarb(Gate *circuit, int numOfGates, FILE *fd)
{

    int i;
    Gate *current;

    fprintf(fd,"%d\n\n",numOfGates);

    for(i=0;i<numOfGates;i++){
        current=circuit+i;
        fprintf(fd,"%d %d\n",current->index,current->type);
        switch (current->type){
            case 0:
                writeInputGate(current,fd);
                break; 
            case 1:
                writeIntermediateGate(current,fd);
                break; 
            case 2:
                writeOutputGate(current,fd);
                break; 
        }
    }
}
