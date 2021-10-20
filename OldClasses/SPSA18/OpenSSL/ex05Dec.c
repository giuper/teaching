#include <openssl/conf.h>
#include <openssl/evp.h>
#include <openssl/err.h>
#include <openssl/pem.h>
#include <openssl/rsa.h>

#include <stdio.h>
#include <string.h>

#include "algorithms.h"

void
readBin(unsigned char *buf,int len, FILE *fp){
    int i,t;
    for(i=0;i<len;i++){
        fscanf(fp,"%d",&t);
        buf[i]=(unsigned char) t;
    }
}


int
main(int argc, char *argv[])
{ 
    ERR_load_crypto_strings();
    OpenSSL_add_all_algorithms();

    if (argc!=3){
        fprintf(stderr,"Usage: %s <privateKey file> <CTfile>\n",argv[0]);
        return 1;
    }


    FILE *privateFile=fopen(argv[1],"r");
    EVP_PKEY *privateKey; 
    privateKey=PEM_read_PrivateKey(privateFile,NULL,NULL,passphrase);
    if (privateKey==NULL){
        fprintf(stderr,"Could not read key from %s\n",argv[1]);
        ERR_print_errors_fp(stderr);
        return 2;
    }

    FILE *ctFile=fopen(argv[2],"r");
    int ciphertext_len;
    fscanf(ctFile,"%d",&ciphertext_len);
    char *ciphertext=malloc(ciphertext_len);
    readBin(ciphertext,ciphertext_len,ctFile);

    EVP_CIPHER_CTX *ctx=EVP_CIPHER_CTX_new();

    if(ctx==NULL){
        fprintf(stderr,"Could not create context\n");
        ERR_print_errors_fp(stderr);
        return 3;
    }


    int eklen=EVP_PKEY_size(privateKey);
    unsigned char *ek=malloc(eklen);
    readBin(ek,eklen,ctFile);
    int ivlen=EVP_CIPHER_iv_length(blockCipher);
    unsigned char *iv=malloc(ivlen);
    readBin(iv,ivlen,ctFile);
    if(1!=EVP_OpenInit(ctx,blockCipher,ek,eklen,iv,privateKey)){
        fprintf(stderr,"Could not init\n");
        ERR_print_errors_fp(stderr);
        return 4;
    }

    unsigned char plaintext[2000];
    int len;
    if(1!=EVP_OpenUpdate(ctx,plaintext,&len,ciphertext,ciphertext_len)){
        fprintf(stderr,"Could not update\n");
        ERR_print_errors_fp(stderr);
        return 5;
    }
    int plaintext_len = len;
    if(1!=EVP_OpenFinal(ctx, plaintext + len, &len)){
        fprintf(stderr,"Could not finalize\n");
        ERR_print_errors_fp(stderr);
        return 6;
    }

    printf("Decrypting: %s\n",plaintext);
        
    return 0;
}
