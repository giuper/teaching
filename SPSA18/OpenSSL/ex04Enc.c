#include <openssl/conf.h>
#include <openssl/evp.h>
#include <openssl/err.h>
#include <openssl/pem.h>

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
        fprintf(stderr,"Usage: %s <pubKey file> <ct file>\n",argv[0]);
        return 1;
    }

    FILE *publicFile=fopen(argv[1],"r");
    EVP_PKEY *publicKey[1]; // an array of one public key
    publicKey[0]=PEM_read_PUBKEY(publicFile,NULL,NULL,NULL);
    if (publicKey[0]==NULL){
        fprintf(stderr,"Could not read key from %s\n",argv[1]);
        ERR_print_errors_fp(stderr);
        return 2;
    } 

    EVP_CIPHER_CTX *ctx=EVP_CIPHER_CTX_new();

    if(ctx==NULL){
        fprintf(stderr,"Could not create context\n");
        ERR_print_errors_fp(stderr);
        return 3;
    }

    int ekl;
    unsigned char *ek[1];
    int lenek=EVP_PKEY_size(publicKey[0]);
    ek[0]=malloc(lenek);
    int leniv=EVP_CIPHER_iv_length(blockCipher);
    unsigned char *iv=malloc(leniv);

    if(1!=EVP_SealInit(ctx,blockCipher,ek,&ekl,iv,publicKey,1)){
        fprintf(stderr,"Could not init\n");
        ERR_print_errors_fp(stderr);
        return 4;
    }

    char ciphertext[2000];
    int len, ciphertext_len;
    printf("Encrypting: %s\n",msgTBE2);
    if(1!=EVP_SealUpdate(ctx, ciphertext, &len,msgTBE2,strlen(msgTBE2)+1)){
        fprintf(stderr,"Could not update\n");
        ERR_print_errors_fp(stderr);
        return 5;
    }
        
    ciphertext_len = len;
    
    if(1 != EVP_SealFinal(ctx, ciphertext + len, &len)){
        fprintf(stderr,"Could not finalize\n");
        ERR_print_errors_fp(stderr);
        return 6;
    }

    ciphertext_len += len;

    EVP_CIPHER_CTX_free(ctx);
    EVP_cleanup();
    CRYPTO_cleanup_all_ex_data();
    ERR_free_strings();

    FILE *ctFile=fopen(argv[2],"w");
    if(ctFile==NULL){
        fprintf(stderr,"Could not open %s\n",argv[2]);
        return 7;
    }
    fprintf(ctFile,"%d\n",ciphertext_len);
    printBinary(ciphertext,ciphertext_len,ctFile);
    printBinary(ek[0],lenek,ctFile);
    printBinary(iv,leniv,ctFile);
    fclose(ctFile);

    return 0;
}
