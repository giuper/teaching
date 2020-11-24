#!/bin/bash
RED='\033[0;31m'   # Red
BLUE='\033[0;34m'  # Blue
GREEN='\033[0;32m' # Green
BROWN='\033[0;33m' # Brown
NC='\033[0m'       # No Color
BOLD='\033[1m'     # Bold

read -p "Name of sender: "
client=${REPLY}

keyfile=otherPrivate/${client}.key.pem
certfile=certs/${client}.cert.pem
cafile=certs/ca-chain.cert.pem
read -p "Name of document: "
doc=${REPLY}

command1="openssl smime -sign -in ${doc} -out ${doc}.sig\
    -signer ${certfile}\
    -inkey ${keyfile} -text"

command2="openssl smime -verify -text -CAfile ${cafile}\
    -in ${doc}.sig -out ${doc}.vrf"

echo -e "${RED}Signing message ${doc}"
echo
echo -e ${BROWN}${command1}
${command1}
echo -e ${NC}


echo
echo
echo -e "${RED}Verifying message ${doc}"
echo
echo -e ${BROWN}${command2}
${command2}
echo -e ${NC}




