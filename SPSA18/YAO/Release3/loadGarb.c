#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "ds.h"
#include "templates.h"

void
readKey(unsigned char *key, FILE *fd){
    int i,t;
     
    for(i=0;i<KEYLEN;i++){
        fscanf(fd,"%d",&t);
        key[i]=(unsigned char) t;
    }
    
}

void
addFunct(Gate *current)
{

    int len;

    len=strlen(current->fName);
            
    if (len==3){
        if (!strcmp(current->fName,"AND")) current->funct=andGate;
        if (!strcmp(current->fName,"NOR")) current->funct=norGate;
        if (!strcmp(current->fName,"XOR")) current->funct=xorGate;
        return;
    }

    if (len==4){
        if (!strcmp(current->fName,"NAND")) current->funct=nandGate;
        if (!strcmp(current->fName,"NXOR")) current->funct=nxorGate;
        return;
    }

    current->funct=orGate;

}

void
loadOutput(Gate *gate, FILE *fd)
{

        fscanf(fd,"%d %d",&(gate->pGate[0]),&(gate->pGate[1]));
        gate->fName=(char *)malloc(6);
        fscanf(fd,"%s",gate->fName);
        gate->table[0][0]=(unsigned char *)malloc(KEYLEN);
        readKey(gate->table[0][0],fd);
        gate->table[0][1]=(unsigned char *)malloc(KEYLEN);
        readKey(gate->table[0][1],fd);
        gate->table[1][0]=(unsigned char *)malloc(KEYLEN);
        readKey(gate->table[1][0],fd);
        gate->table[1][1]=(unsigned char *)malloc(KEYLEN);
        readKey(gate->table[1][1],fd);
}


Gate *
loadCircuit(FILE *fd, int *l,int *y)
{

    int i,t,len;
    Gate *current;
    fscanf(fd,"%d",l);  //number of gates 

    Gate *circuit=malloc(*l*sizeof(Gate));

    for(i=0;i<*l;i++){
        current=circuit+i;

        fscanf(fd,"%d %d",&(current->index),&(current->type));
        if(current->type==2){
            loadOutput(current,fd);
            addFunct(current);
            continue;
        }

        // it's an input gate
        fscanf(fd,"%d",&(current->yIndex));
        fscanf(fd,"%d %d",&(current->nGate[0]),&(current->nGate[1]));
        current->fName=(char *)malloc(6);
        fscanf(fd,"%s",current->fName);
        current->table[y[current->yIndex]][0]=(unsigned char *)malloc(KEYLEN);
        readKey(current->table[y[current->yIndex]][0],fd);
        fscanf(fd,"%d",&t);
        current->table[y[current->yIndex]][1]=(unsigned char *)malloc(1);
        current->table[y[current->yIndex]][1][0]=(unsigned char)t;
        addFunct(current);
    }
    return circuit;

}
