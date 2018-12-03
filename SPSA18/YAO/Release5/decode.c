#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <openssl/conf.h>
#include <openssl/evp.h>
#include <openssl/err.h>
#include <openssl/rand.h>

#include "ds.h"
#include "templates.h"


Wire *
decodeOther(Gate *circuit, int gateIndex)
{

    Wire *wire=(Wire *)malloc(sizeof(Wire));
    Gate *current=circuit+gateIndex;

    if (0==current->type){   //input gate
        wire->key=current->table[0][0];
        wire->gb=*current->table[0][1];
#ifdef DEBUG
        printf("Input gate %d\n",current->index);
        BIO_dump_fp (stdout,(const char *)wire->key,KEYLEN);
        printf("%d\n",wire->gb);
#endif
        return wire;
    }

    if (1==current->type){   //intermediate gate
        Wire *wirel=decodeOther(circuit,current->pGate[0]);
        Wire *wirer=decodeOther(circuit,current->pGate[1]);

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

    //should not reach here
    free(wire);
    return (Wire *)NULL;

}

int
decode(Gate *circuit, int gateIndex)
{

    Gate *current=circuit+gateIndex;

    if (2!=current->type) return -1; 

    Wire *wirel=decodeOther(circuit,current->pGate[0]);
    Wire *wirer=decodeOther(circuit,current->pGate[1]);

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

