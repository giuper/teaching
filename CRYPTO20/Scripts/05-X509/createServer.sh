#!/bin/bash

read -p "Name of server: "
server=${REPLY}

serverKey=otherPrivate/${server}.key.pem
csrfile=csr/${server}.csr.pem
certfile=certs/${server}.cert.pem
configFile=./opensslIntermediate.cnf
certchain=certs/ca-chain.cert.pem

echo "Generating the private key for the server"
openssl genrsa -out ${serverKey} 2048
chmod 400 ${serverKey}

read -p "Press enter to continue "
clear
echo
echo "Generating the server's CSR"

openssl req -config ${configFile} \
    -key ${serverKey} \
    -new -sha256 -out ${csrfile}

read -p "Press enter to continue "
clear
echo
echo "Signing the CSR with the key of the Intermediate CA"

openssl ca -config ${configFile}\
    -extensions server_cert -days 375 -notext -md sha256\
    -in ${csrfile} \
    -out ${certfile}

chmod 444 ${certfile}

read -p "Press enter to continue "
clear
echo
echo "Inspecting the server's certificate"
openssl x509 -noout -text -in ${certfile}


read -p "Press enter to continue "
clear
echo
echo "Verifying the server's certificate"
openssl verify -CAfile ${certchain} ${certfile}

