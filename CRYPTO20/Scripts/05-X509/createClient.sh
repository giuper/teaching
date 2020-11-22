#!/bin/bash

read -p "Name of client: "
client=${REPLY}

keyfile=otherPrivate/${client}.key.pem
csrfile=csr/${client}.csr.pem
certfile=certs/${client}.cert.pem
configFile=./opensslIntermediate.cnf


echo "Generating the private key for the client"
openssl genrsa -out ${keyfile} 2048
chmod 400 ${keyfile}

read -p "Press enter to continue "
clear
echo
echo "Generating the CSR for the client"

openssl req -config ${configFile} \
    -key ${keyfile} \
    -new -sha256 -out ${csrfile}

read -p "Press enter to continue "
clear
echo
echo "Signing the CSR with the Intermediate CA"

openssl ca -config ${configFile}\
    -extensions usr_cert -days 375 -notext -md sha256\
    -in ${csrfile} \
    -out ${certfile}

chmod 444 ${certfile}

read -p "Press enter to continue "
clear
echo
echo "Inspecting the certificate of the Intermediate CA"
openssl x509 -noout -text -in ${certfile}


read -p "Press enter to continue "
clear
echo
echo "Verifying the certificate of the Intermediate CA"
openssl verify -CAfile certs/ca-chain.cert.pem ${certfile}


