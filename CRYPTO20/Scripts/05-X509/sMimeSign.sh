#!/bin/bash

read -p "Name of sender: "
client=${REPLY}

keyfile=otherPrivate/${client}.key.pem
certfile=certs/${client}.cert.pem
cafile=certs/ca-chain.cert.pem
read -p "Name of document: "
doc=${REPLY}

echo "Signing message ${doc}"

openssl smime -sign -in ${doc} -out ${doc}.sig\
    -signer ${certfile}\
    -inkey ${keyfile} -text

openssl smime -verify -text -CAfile ${cafile}\
    -in ${doc}.sig -out ${doc}.vrf




