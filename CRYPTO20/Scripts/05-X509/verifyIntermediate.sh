#!/bin/bash

intermediateCert=certs/intermediate.cert.pem
rootCert=../certs/cacert.pem
chainCert=certs/ca-chain.cert.pem

echo "Inspecting the certificate for the Intermediate CA"
openssl x509 -noout -text -in ${intermediateCert}


read -p "Press enter to continue "
clear
echo
echo "Verifying the certificate for the Intermediate CA against the ROOT CA"
openssl verify -CAfile ${rootCert} ${intermediateCert}
echo

read -p "Press enter to continue "
clear
echo "Constructing the certificate chain file"
cat ${intermediateCert} ${rootCert} > ${chainCert}
chmod 444 ${chainCert}
echo
echo

