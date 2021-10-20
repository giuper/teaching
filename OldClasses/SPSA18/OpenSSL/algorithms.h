#define blockCipher EVP_aes_256_cbc()           /* block cipher for hybrid encryption */
#define MDAlgo EVP_sha256()                     /* hash algorithm for signatures */
#define armorAlgo EVP_aes_256_cbc()             /* armor algorithm for storing private keys */

char passphrase[]="SPSA18--password";             /* pass phrase for storing private keys */

#define KEYLEN 2048                               /* lenght of asymmetric keys */

char msgTBE[]="SPSA18--Prova di cifratura";       /* message to be encrypted */
char msgTBE2[]="SPSA18--Prova di cifratura--EVP"; /* message to be encrypted with EVP*/
char msgTBS[]="SPSA18--Firma";                    /* message to be signed */


