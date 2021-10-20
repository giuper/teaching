#include <openssl/evp.h>
#include <openssl/dsa.h>
#include <openssl/pem.h>

#include <stdio.h>
#include "algorithms.h"

int
main(int argc,char *argv[])
{

    if (argc!=4){
        fprintf(stderr,"Usage: %s <publicKey file> <privateKey file> <privateUnKey file>\n",argv[0]);
        return 1;
    }


    OpenSSL_add_all_algorithms();

    EVP_PKEY_CTX *ctx_params=EVP_PKEY_CTX_new_id(EVP_PKEY_DSA, NULL);
    EVP_PKEY_CTX_set_dsa_paramgen_bits(ctx_params,KEYLEN);
    EVP_PKEY_paramgen_init(ctx_params);
    EVP_PKEY* pkey_params=NULL;
    EVP_PKEY_paramgen(ctx_params, &pkey_params);

    EVP_PKEY_CTX *ctx=EVP_PKEY_CTX_new(pkey_params,NULL);
    EVP_PKEY_keygen_init(ctx);
    EVP_PKEY* pkey=NULL;
    EVP_PKEY_keygen(ctx,&pkey);

    EVP_PKEY_free(pkey_params);
    EVP_PKEY_CTX_free(ctx_params);
    EVP_PKEY_CTX_free(ctx);

    FILE *publicFile=fopen(argv[1],"w");
    FILE *privateFile=fopen(argv[2],"w");
    FILE *private_unFile=fopen(argv[3],"w");

    if(publicFile==NULL)
        fprintf(stderr,"Could not open %s\n",argv[1]);
    else{
        PEM_write_PUBKEY(publicFile,pkey);
        fclose(publicFile);
    }

    if(privateFile==NULL)
        fprintf(stderr,"Could not open %s\n",argv[2]);
    else {
        PEM_write_PrivateKey(privateFile,pkey,armorAlgo,NULL,0,NULL,passphrase);
        fclose(privateFile);
    }

    if(private_unFile==NULL)
        fprintf(stderr,"Could not open %s\n",argv[3]);
    else {
        PEM_write_PrivateKey(private_unFile,pkey,NULL,NULL,0,NULL,NULL);
        fclose(private_unFile);
    }

    EVP_cleanup();
    CRYPTO_cleanup_all_ex_data();

    return 0;
}

