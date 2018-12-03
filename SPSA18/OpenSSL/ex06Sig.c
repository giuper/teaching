#include <openssl/conf.h>
#include <openssl/evp.h>
#include <openssl/err.h>
#include <openssl/pem.h>
#include <openssl/rsa.h>

#include <stdio.h>
#include <string.h>

#include "algorithms.h"

void
printBinary(unsigned char *buf, int len, FILE *fp)
{
    int i;
    for(i=0;i<len;i++) fprintf(fp,"%d ",(unsigned int) buf[i]);
    fprintf(fp,"\n");
}

int
main(int argc, char *argv[])
{ 
    ERR_load_crypto_strings();
    OpenSSL_add_all_algorithms();


    if(argc!=3){
        fprintf(stderr,"Usage: %s <file PrivateKey> <file Signature>\n",argv[0]);
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

    EVP_MD_CTX *mdctx = NULL;
 
    char *sig = NULL;
 
    if(!(mdctx = EVP_MD_CTX_create())){
        fprintf(stderr,"Could not create context\n");
        return 1;
    }
 
    if(1 != EVP_DigestSignInit(mdctx,NULL,MDAlgo,NULL,privateKey)){
        fprintf(stderr,"Could not create init\n");
        return 1;
    }
 
    printf("Message signed: %s\n",msgTBS);
    if(1 != EVP_DigestSignUpdate(mdctx, msgTBS, strlen(msgTBS))){
        fprintf(stderr,"Could not create update\n");
        return 1;
    }
 
    int slen;
    if(1 != EVP_DigestSignFinal(mdctx,NULL,&slen)){
        fprintf(stderr,"Could not finalize\n");
        return 1;
    }

    sig=malloc(slen);
    
    if(1!=EVP_DigestSignFinal(mdctx,sig,&slen)){
        fprintf(stderr,"Could not finalize2\n");
        return 1;
    }
 
    FILE *signatureFile=fopen(argv[2],"w");
    fprintf(signatureFile,"%d\n",slen);
    printBinary(sig,slen,signatureFile);
    fclose(signatureFile);
    
    return 0;
}
