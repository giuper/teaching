#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <openssl/conf.h>
#include <openssl/evp.h>
#include <openssl/err.h>
#include <openssl/rand.h>
#include "ds.h"
#include "templates.h"

void encodeOutput(Gate *,Gate *);
void encodeInput(Gate *,Gate *,int *);
void encodeIntermediate(Gate *,Gate *);

/* circuit is the circuit
   l is the number of gates in the circuit
   x is the 0/1 assignment to the x1,x2,...
*/

void
encode(Gate *circuit,int *x,int numOfGates)
{

    int i;
    Gate *current;

    for(i=0;i<numOfGates;i++){
        current=circuit+i;

        RAND_bytes((unsigned char *)current->gb,4);
        current->gb[0]%=2;
        RAND_bytes((unsigned char *)((current->gb)+1),4);
        current->gb[1]%=2;

        current->keys[0]=(unsigned char *)malloc(KEYLEN);
        current->keys[1]=(unsigned char *)malloc(KEYLEN);
        RAND_bytes((unsigned char *)current->keys[0],KEYLEN);
        RAND_bytes((unsigned char *)current->keys[1],KEYLEN);

#ifdef DEBUG
printf("Gate %d\n",i);
printf("Key 0\n");
BIO_dump_fp (stdout,(const char *)current->keys[0],KEYLEN);
printf("Key 1\n");
BIO_dump_fp (stdout,(const char *)current->keys[1],KEYLEN);
printf("Garbling bit 0: %d\n",current->gb[0]);
printf("Garbling bit 1: %d\n",current->gb[1]);
printf("\n\n");
#endif

    }

    for(i=0;i<numOfGates;i++){
        current=circuit+i;
        switch (current->type){
            case 0:
                encodeInput(circuit,current,x);
                break;

            case 1:
                encodeIntermediate(circuit,current);
                break;

            case 2:
                encodeOutput(circuit,current);
                break;
        }
    }

}

   

void
encodeOutput(Gate *circuit,Gate *current)
{

    int b0,b1;
    int r,c;
    int res;
    Gate *p0,*p1;
    unsigned char *plaintext =(unsigned char *)malloc(KEYLEN);
    unsigned char *ciphertext=(unsigned char *)malloc(KEYLEN);

    b0=current->gb[0]; p0=circuit+current->pGate[0]; 
    b1=current->gb[1]; p1=circuit+current->pGate[1];
    for(r=0;r<2;r++){
        for(c=0;c<2;c++){
            res=current->funct(r^b0,c^b1);     
            RAND_bytes((unsigned char *)plaintext,KEYLEN);
            plaintext[KEYLEN-1]=(unsigned char)res;
            current->table[r][c]=(unsigned char *)malloc(KEYLEN);
            ECBencrypt(plaintext,KEYLEN,p1->keys[c^b1],ciphertext);
            ECBencrypt(ciphertext,KEYLEN,p0->keys[r^b0],current->table[r][c]);
#ifdef DEBUG
            printf("Output gate %d\ttable[%d][%d] holding result for (%d,%d)\n",current->index,r,c,b0^r,b1^c);
            printf("Plaintext: \n");
            BIO_dump_fp (stdout,(const char *)plaintext,KEYLEN);
            printf("Last byte: %d\n",(int) plaintext[KEYLEN-1]);
            printf("with key:\n");
            BIO_dump_fp (stdout,(const char *)p1->keys[c^b1],KEYLEN);
            printf("obtaining:\n");
            BIO_dump_fp (stdout,(const char *)ciphertext,KEYLEN);
            printf("with key:\n");
            BIO_dump_fp (stdout,(const char *)p0->keys[r^b0],KEYLEN);
            printf("obtaining:\n");
            BIO_dump_fp (stdout,(const char *)current->table[r][c],KEYLEN);
            printf("\n\n\n");
#endif
        }
    }
}


void
encodeInput(Gate *circuit,Gate *current,int *x)
{

    int res;
    int yinp,xinp=x[current->xIndex];
    Gate *ng=circuit+current->nGate[0];
    int ngb=ng->gb[current->nGate[1]];

    for(yinp=0;yinp<2;yinp++){
        res=current->funct(xinp,yinp);
        current->table[yinp][0]=(unsigned char *)malloc(KEYLEN);
        memcpy(current->table[yinp][0],current->keys[res],KEYLEN);
         current->table[yinp][1]=(unsigned char *)malloc(1);
        *current->table[yinp][1]=(unsigned char) res^ngb;
    }

#ifdef DEBUG
    printf("Input gate %d\n",current->index);
    printf("Key 0:\n");
    BIO_dump_fp (stdout,(const char *)current->keys[0],KEYLEN);
    printf("Key 1:\n");
    BIO_dump_fp (stdout,(const char *)current->keys[1],KEYLEN);
    printf("\n\n");
#endif

}

void
encodeIntermediate(Gate *circuit,Gate *current)
{

    int b0,b1;
    int r,c;
    int res;
    Gate *p0,*p1, *next;
    unsigned char *plaintext =(unsigned char *)malloc(2*KEYLEN);
    unsigned char *ciphertext=(unsigned char *)malloc(2*KEYLEN);

    b0=current->gb[0]; p0=circuit+current->pGate[0]; 
    b1=current->gb[1]; p1=circuit+current->pGate[1];
    next=circuit+current->nGate[0];
    unsigned int ngb=next->gb[current->nGate[1]];

    for(r=0;r<2;r++){
        for(c=0;c<2;c++){
            res=current->funct(r^b0,c^b1);     
            memcpy(plaintext,current->keys[res],KEYLEN);
            RAND_bytes(plaintext+KEYLEN,KEYLEN);
            plaintext[2*KEYLEN-1]=(unsigned char)res^ngb;
            current->table[r][c]=(unsigned char *)malloc(2*KEYLEN);
            ECBencrypt(plaintext,2*KEYLEN,p1->keys[c^b1],ciphertext);
            ECBencrypt(ciphertext,2*KEYLEN,p0->keys[r^b0],current->table[r][c]);
#ifdef DEBUG
            printf("Intermediate gate %d\ttable[%d][%d] holding result for (%d,%d)\n",current->index,r,c,b0^r,b1^c);
            printf("Plaintext: \n");
            BIO_dump_fp (stdout,(const char *)plaintext,2*KEYLEN);
            printf("with key:\n");
            BIO_dump_fp (stdout,(const char *)p1->keys[c^b1],KEYLEN);
            printf("obtaining:\n");
            BIO_dump_fp (stdout,(const char *)ciphertext,2*KEYLEN);
            printf("with key:\n");
            BIO_dump_fp (stdout,(const char *)p0->keys[r^b0],KEYLEN);
            printf("obtaining:\n");
            BIO_dump_fp (stdout,(const char *)current->table[r][c],2*KEYLEN);
            printf("\n\n\n");
#endif
        }
    }
}
