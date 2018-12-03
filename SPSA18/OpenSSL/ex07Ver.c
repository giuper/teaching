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
main(int argc, char *argv[]){ 
    ERR_load_crypto_strings();
    OpenSSL_add_all_algorithms();
    //OPENSSL_config(NULL);

    if(argc!=3){
        fprintf(stderr,"Usage: %s <file PublicKey> <file Signature>\n",argv[0]);
        return 1;
    }

    FILE *publicFile=fopen(argv[1],"r");
    EVP_PKEY *publicKey; 
    publicKey=PEM_read_PUBKEY(publicFile,NULL,NULL,NULL);
    if (publicKey==NULL){
        fprintf(stderr,"Could not read key from %s\n",argv[1]);
        ERR_print_errors_fp(stderr);
        return 2;
    }

    FILE *signatureFile=fopen(argv[2],"r");
    int slen;
    fscanf(signatureFile,"%d",&slen);
    unsigned char *sig=malloc(slen);
    readBin(sig,slen,signatureFile);
    fclose(signatureFile);
    
    EVP_MD_CTX *mdctx = NULL;
    if(!(mdctx = EVP_MD_CTX_create())){
        fprintf(stderr,"Could not create context\n");
        ERR_print_errors_fp(stderr);
        return 3;
    }
 
    if(1!=EVP_DigestVerifyInit(mdctx,NULL,MDAlgo,NULL,publicKey)){
        fprintf(stderr,"Could not initialize\n");
        ERR_print_errors_fp(stderr);
        return 4;
    }

    if(1!=EVP_DigestVerifyUpdate(mdctx,msgTBS,strlen(msgTBS))){
        fprintf(stderr,"Could not verify\n");
        ERR_print_errors_fp(stderr);
        return 5;
    }

    if(1==EVP_DigestVerifyFinal(mdctx,sig,slen)){
        fprintf(stdout,"Successful verification of message: %s\n",msgTBS);
    }
    else{
        fprintf(stdout,"UnSuccessful verification of message: %s\n",msgTBS);
    }

}
