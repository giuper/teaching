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
printKey(unsigned char *key, FILE *fd){

    int i;
    for(i=0;i<KEYLEN;i++)
        fprintf(fd,"%d ",(unsigned int) key[i]);
    fprintf(fd,"\n");

}

void
printOutputGate(Gate *gate, FILE *fd)
{

        fprintf(fd,"%d %d\n",gate->pGate[0],gate->pGate[1]);
        fprintf(fd,"%s\n",gate->fName);
        printKey(gate->table[0][0],fd);
        printKey(gate->table[0][1],fd);
        printKey(gate->table[1][0],fd);
        printKey(gate->table[1][1],fd);

}

void
fSelect(Gate *circuit, int *y, int l, FILE *fd)
{

    int i;
    Gate *current;

    fprintf(fd,"%d\n\n",l);
    for(i=0;i<l;i++){
        current=circuit+i;

        fprintf(fd,"%d %d\n",current->index,current->type);

        if(current->type==2){
            printOutputGate(current,fd);
            fprintf(fd,"\n");
            continue;
        }
/* it is an input gate */
        fprintf(fd,"%d\n",current->yIndex);
        fprintf(fd,"%d %d\n",current->nGate[0],current->nGate[1]);
        fprintf(fd,"%s\n",current->fName);
        printKey(current->table[y[current->yIndex]][0],fd);
        fprintf(fd,"%d\n",*(current->table[y[current->yIndex]][1]));
        fprintf(fd,"\n");
        

    }
}
