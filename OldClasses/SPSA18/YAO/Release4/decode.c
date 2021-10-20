#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <openssl/conf.h>
#include <openssl/evp.h>
#include <openssl/err.h>
#include <openssl/rand.h>

#include "ds.h"
#include "templates.h"

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
    unsigned char *K0=(unsigned char *)malloc(KEYLEN);
    memcpy(K0,input0->table[y0][0],KEYLEN);

    int y1=y[input1->yIndex];
    unsigned char *K1=(unsigned char *)malloc(KEYLEN);
    memcpy(K1,input1->table[y1][0],KEYLEN);
    int ROW=*(input0->table[y0][1]);
    int COL=*(input1->table[y1][1]);

    unsigned char *ciphertext=(unsigned char *)malloc(KEYLEN);
    ECBdecrypt(output->table[ROW][COL],KEYLEN,K0,ciphertext);
    unsigned char *plaintext=(unsigned char *)malloc(KEYLEN);
    ECBdecrypt(ciphertext,KEYLEN,K1,plaintext);

#ifdef DEBUG
    printf("Decrypting table[%d][%d]\n",ROW,COL);
    printf("Ciphertext: \n");
    BIO_dump_fp (stdout,output->table[ROW][COL],KEYLEN);
    printf("with key:\n");
    BIO_dump_fp (stdout,(const char *)K0,KEYLEN);
    printf("obtaining:\n");
    BIO_dump_fp (stdout,(const char *)ciphertext,KEYLEN);
    printf("with key:\n");
    BIO_dump_fp (stdout,(const char *)K1,KEYLEN);
    printf("obtaining:\n");
    BIO_dump_fp (stdout,(const char *)plaintext,KEYLEN);
#endif

    return plaintext[KEYLEN-1];
    
}

Wire *
decodeOther(Gate *circuit, int i, int *y)
{

    Wire *wire=(Wire *)malloc(sizeof(Wire));
    Gate *current=circuit+i;

    if (0==current->type){   //input gate
        int y0=y[current->yIndex];
        wire->key=current->table[y0][0];
        wire->gb=*current->table[y0][1];
#ifdef DEBUG
        printf("Input gate %d\n",current->index);
        BIO_dump_fp (stdout,(const char *)wire->key,KEYLEN);
        printf("%d\n",wire->gb);
#endif
        return wire;
    }

    if (1==current->type){   //intermediate gate
        Wire *wirel=decodeOther(circuit,current->pGate[0],y);
        Wire *wirer=decodeOther(circuit,current->pGate[1],y);

        int ROW=wirel->gb; unsigned char *K0=wirel->key;
        int COL=wirer->gb; unsigned char *K1=wirer->key;
    
    
        unsigned char *ciphertext=(unsigned char *)malloc(2*KEYLEN);
        ECBdecrypt(current->table[ROW][COL],2*KEYLEN,K0,ciphertext);
        unsigned char *plaintext=(unsigned char *)malloc(2*KEYLEN);
        ECBdecrypt(ciphertext,2*KEYLEN,K1,plaintext);
#ifdef DEBUG
        printf("Intermediate gate %d\t",current->index);
        printf("looking at table[%d][%d]\n",ROW,COL);
        BIO_dump_fp (stdout,(const char *)current->table[ROW][COL],2*KEYLEN);
        printf("decrypting with key\n");
        BIO_dump_fp (stdout,(const char *)K0,KEYLEN);
        printf("obtaining\n");
        BIO_dump_fp (stdout,(const char *)ciphertext,2*KEYLEN);
        printf("decrypting with key\n");
        BIO_dump_fp (stdout,(const char *)K1,KEYLEN);
        printf("obtaining\n");
        BIO_dump_fp (stdout,(const char *)plaintext,2*KEYLEN);
#endif

        wire->key=plaintext;
        wire->gb=plaintext[2*KEYLEN-1];
        return wire;
    }

    free(wire);
    return (Wire *)NULL;

}

int
decode(Gate *circuit, int i, int *y)
{

    Gate *current=circuit+i;

    if (2!=current->type) return -1; 

    Wire *wirel=decodeOther(circuit,current->pGate[0],y);
    Wire *wirer=decodeOther(circuit,current->pGate[1],y);

    int ROW=wirel->gb; unsigned char *K0=wirel->key;
    int COL=wirer->gb; unsigned char *K1=wirer->key;
    
    
    unsigned char *ciphertext=(unsigned char *)malloc(KEYLEN);
    ECBdecrypt(current->table[ROW][COL],KEYLEN,K0,ciphertext);
    unsigned char *plaintext=(unsigned char *)malloc(KEYLEN);
    ECBdecrypt(ciphertext,KEYLEN,K1,plaintext);

#ifdef DEBUG
        printf("Output gate %d\t",current->index);
        printf("looking at table[%d][%d]\n",ROW,COL);
        BIO_dump_fp (stdout,(const char *)current->table[ROW][COL],KEYLEN);
        printf("decrypting with key\n");
        BIO_dump_fp (stdout,(const char *)K0,KEYLEN);
        printf("obtaining\n");
        BIO_dump_fp (stdout,(const char *)ciphertext,KEYLEN);
        printf("decrypting with key\n");
        BIO_dump_fp (stdout,(const char *)K1,KEYLEN);
        printf("obtaining\n");
        BIO_dump_fp (stdout,(const char *)plaintext,KEYLEN);
#endif

    return plaintext[KEYLEN-1];
}

