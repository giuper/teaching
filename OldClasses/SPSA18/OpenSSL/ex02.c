#include <openssl/conf.h>
#include <openssl/evp.h>
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

    BIO *b=BIO_new(BIO_s_file());
    BIO_set_fp(b,stdout,BIO_NOCLOSE);

    if(publicKey!=NULL){
        printf("Printing the public key\n");
        EVP_PKEY_print_public(b,publicKey,4,NULL);
        printf("\n\n");
    }
    if(privateKey!=NULL){
        printf("Printing the private key\n");
        EVP_PKEY_print_private(b,privateKey,4,NULL);
    }

    EVP_cleanup();
    CRYPTO_cleanup_all_ex_data();

    return 0;
}
