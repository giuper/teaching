#!/usr/bin/bash

caKey="private/intermediate.key.pem"
csr="csr/intermediate.csr.pem"
configFile="./opensslIntermediate.cnf"


echo "Generating the private key for the Intermediate CA"
openssl genrsa -aes256 -out ${caKey} 4096
chmod 400 ${caKey}

echo
echo
echo "Generating a CSR for the Intermediate CA"
openssl req -config ${configFile} -new -sha256 \
    -key ${caKey}\
    -out ${csr}

