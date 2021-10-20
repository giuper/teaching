#include <openssl/conf.h>
#include <openssl/evp.h>
#include <openssl/err.h>
#include <openssl/pem.h>
#include <openssl/rsa.h>

#include <stdio.h>
#include <string.h>
#include "algorithms.h"

int
main(int argc, char *argv[])
{ 
    ERR_load_crypto_strings();
    OpenSSL_add_all_algorithms();

    if(argc!=3){
        fprintf(stderr,"Usage: %s <publicKey file> <privateKey file>\n",argv[0]);
        return 1;
    }

    FILE *publicFile=fopen(argv[1],"r");
    FILE *privateFile=fopen(argv[2],"r");

    EVP_PKEY *publicKey=PEM_read_PUBKEY(publicFile,NULL,NULL,NULL);
    if (publicKey==NULL){
        fprintf(stderr,"Could not read key from %s\n",argv[1]);
        return 2;
    }

    EVP_PKEY *privateKey=PEM_read_PrivateKey(privateFile,NULL,NULL,passphrase);
    if (privateKey==NULL){
        fprintf(stderr,"Could not read key from %s\n",argv[2]);
        return 2;
    }

    RSA *rsaPublic=EVP_PKEY_get1_RSA(publicKey);
    unsigned char to[RSA_size(rsaPublic)];
    unsigned char final[256];
    int len;

    printf("Encrypting: %s\n",msgTBE);
    if ((len=RSA_public_encrypt(strlen(msgTBE)+1,msgTBE,to,rsaPublic,RSA_PKCS1_OAEP_PADDING))==-1){
        char *err = (char *)malloc(130);
        ERR_error_string(ERR_get_error(), err);
        fprintf(stderr, "Error encrypting message: %s\n", err);
        return 3;
    }
    

    RSA *rsaPrivate=EVP_PKEY_get1_RSA(privateKey);

    if(RSA_private_decrypt(len,to,final,rsaPrivate,RSA_PKCS1_OAEP_PADDING)==-1){
        char *err = (char *)malloc(130);
        ERR_error_string(ERR_get_error(), err);
        fprintf(stderr, "Error encrypting message: %s\n", err);
        return 4;
    }

    printf("Decrypting: %s\n",final);

    EVP_cleanup();
    CRYPTO_cleanup_all_ex_data();
    ERR_free_strings();

    return 0;
}
