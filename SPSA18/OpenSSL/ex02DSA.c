#include <openssl/conf.h>
#include <openssl/evp.h>
#include <openssl/err.h>
#include <openssl/pem.h>

#include <stdio.h>
#include "algorithms.h"

int
main(int argc, char *argv[])
{ 

    if (argc!=3){
        fprintf(stderr,"Usage: %s <publicKey file> <privateKey file>\n",argv[0]);
        return 1;
    }

    OpenSSL_add_all_algorithms();

    FILE *publicFile=fopen(argv[1],"r");
    FILE *privateFile=fopen(argv[2],"r");

    EVP_PKEY *publicKey=PEM_read_PUBKEY(publicFile,NULL,NULL,NULL);
    EVP_PKEY *privateKey=PEM_read_PrivateKey(privateFile,NULL,NULL,passphrase);

    if(publicKey!=NULL){
        printf("Printing the public key\n");
        DSA *dsa=EVP_PKEY_get1_DSA(publicKey);
        BIO *b=BIO_new(BIO_s_file());
        BIO_set_fp(b,stdout,BIO_NOCLOSE);
        DSA_print(b,dsa,0);
        printf("\n");
    }

    if(privateKey!=NULL){
        printf("Printing the private key\n");
        DSA *dsa=EVP_PKEY_get1_DSA(privateKey);
        BIO *b=BIO_new(BIO_s_file());
        BIO_set_fp(b,stdout,BIO_NOCLOSE);
        DSA_print(b,dsa,0);
        printf("\n\n");
    }


    return 0;
}
