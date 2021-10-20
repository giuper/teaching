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

    //if (plaintext[KEYLEN-1]&(unsigned char)0x01)
    if (plaintext[KEYLEN-1]==(unsigned char)0x01)
        return 1;
    else
        return 0;

//    return plaintext[KEYLEN-1];
}
