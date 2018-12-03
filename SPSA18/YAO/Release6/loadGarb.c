#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "ds.h"
#include "templates.h"

void
readKey(unsigned char *key, int len,FILE *fd){
    int i,t;
     
    for(i=0;i<len;i++){
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
loadInput(Gate *gate, FILE *fd)
{
        int t;

        fscanf(fd,"%d",&(gate->yIndex));
        fscanf(fd,"%d %d",&(gate->nGate[0]),&(gate->nGate[1]));
        gate->fName=(char *)malloc(6);
        fscanf(fd,"%s",gate->fName);
        gate->table[0][0]=(unsigned char *)malloc(KEYLEN);
        readKey(gate->table[0][0],KEYLEN,fd);
        fscanf(fd,"%d",&t);
        gate->table[0][1]=(unsigned char *)malloc(1);
        gate->table[0][1][0]=(unsigned char)t;
        gate->table[1][0]=NULL;
        gate->table[1][1]=NULL;
        addFunct(gate);
}

void
loadIntermediate(Gate *gate, FILE *fd)
{

        fscanf(fd,"%d %d",&(gate->pGate[0]),&(gate->pGate[1]));
        fscanf(fd,"%d %d",&(gate->nGate[0]),&(gate->nGate[1]));
        gate->fName=(char *)malloc(6);
        fscanf(fd,"%s",gate->fName);
        gate->table[0][0]=(unsigned char *)malloc(2*KEYLEN);
        readKey(gate->table[0][0],2*KEYLEN,fd);
        gate->table[0][1]=(unsigned char *)malloc(2*KEYLEN);
        readKey(gate->table[0][1],2*KEYLEN,fd);
        gate->table[1][0]=(unsigned char *)malloc(2*KEYLEN);
        readKey(gate->table[1][0],2*KEYLEN,fd);
        gate->table[1][1]=(unsigned char *)malloc(2*KEYLEN);
        readKey(gate->table[1][1],2*KEYLEN,fd);
        addFunct(gate);
}


void
loadOutput(Gate *gate, FILE *fd)
{

        fscanf(fd,"%d %d",&(gate->pGate[0]),&(gate->pGate[1]));
        gate->fName=(char *)malloc(6);
        fscanf(fd,"%s",gate->fName);
        gate->table[0][0]=(unsigned char *)malloc(KEYLEN);
        readKey(gate->table[0][0],KEYLEN,fd);
        gate->table[0][1]=(unsigned char *)malloc(KEYLEN);
        readKey(gate->table[0][1],KEYLEN,fd);
        gate->table[1][0]=(unsigned char *)malloc(KEYLEN);
        readKey(gate->table[1][0],KEYLEN,fd);
        gate->table[1][1]=(unsigned char *)malloc(KEYLEN);
        readKey(gate->table[1][1],KEYLEN,fd);
        addFunct(gate);
}


Gate *
readGarb(FILE *fd, int *numOfGates)
{

    int i,len;
    Gate *current;
    fscanf(fd,"%d",numOfGates);  //number of gates 

    Gate *circuit=malloc(*numOfGates*sizeof(Gate));

    for(i=0;i<*numOfGates;i++){
        current=circuit+i;

        fscanf(fd,"%d %d",&(current->index),&(current->type));
        switch (current->type){
            case 0:
                loadInput(current,fd);
                break;
            case 1:
                loadIntermediate(current,fd);
                break;
            case 2:
                loadOutput(current,fd);
                break;
        }
    }
    return circuit;
}
