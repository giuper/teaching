#!/bin/bash

read -p "Name of recipient: "
client=${REPLY}

keyfile=otherPrivate/${client}.key.pem
certfile=certs/${client}.cert.pem

read -p "Name of document: "
doc=${REPLY}

echo "Encrypting message ${doc}"

openssl smime -binary -encrypt -in ${doc} -out ${doc}.cpt ${certfile}

echo "Decrypting message ${doc}.cpt"
openssl smime -binary -decrypt -in ${doc}.cpt -recip ${certfile} -inkey ${keyfile} -out ${doc}.new

