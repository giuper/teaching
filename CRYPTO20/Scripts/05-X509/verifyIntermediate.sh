#!/bin/bash
RED='\033[0;31m'   # Red
BLUE='\033[0;34m'  # Blue
GREEN='\033[0;32m' # Green
BROWN='\033[0;33m' # Brown
NC='\033[0m'       # No Color
BOLD='\033[1m'     # Bold

intermediateCert=certs/intermediate.cert.pem
rootCert=../certs/cacert.pem
chainCert=certs/ca-chain.cert.pem

command1="openssl x509 -noout -text -in ${intermediateCert}"
command2="openssl verify -CAfile ${rootCert} ${intermediateCert}"

echo -e "${RED}Inspecting the certificate for the Intermediate CA"
echo
echo -e ${BROWN}${command1}${NC}
${command1}


read -p "Press enter to continue "
clear
echo
echo -e "${RED}Verifying the certificate for the Intermediate CA against the ROOT CA"
echo
echo -e ${BROWN}${command2}${NC}
${command2}
echo

read -p "Press enter to continue "
clear
echo -e "${RED}Constructing the certificate chain file"
cat ${intermediateCert} ${rootCert} > ${chainCert}
chmod 444 ${chainCert}
echo
echo

