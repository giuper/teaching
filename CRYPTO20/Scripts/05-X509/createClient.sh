#!/bin/bash
RED='\033[0;31m'   # Red
BLUE='\033[0;34m'  # Blue
GREEN='\033[0;32m' # Green
BROWN='\033[0;33m' # Brown
NC='\033[0m'       # No Color
BOLD='\033[1m'     # Bold

read -p "Name of client: "
client=${REPLY}

keyfile=otherPrivate/${client}.key.pem
csrfile=csr/${client}.csr.pem
certfile=certs/${client}.cert.pem
configFile=./opensslIntermediate.cnf

command1="openssl genrsa -out ${keyfile} 2048"
command2="openssl req -config ${configFile} \
    -key ${keyfile} \
    -new -sha256 -out ${csrfile}"
command3="openssl ca -config ${configFile}\
    -extensions usr_cert -days 375 -notext -md sha256\
    -in ${csrfile} \
    -out ${certfile}"
command4="openssl x509 -noout -text -in ${certfile}"
command5="openssl verify -CAfile certs/ca-chain.cert.pem ${certfile}"

echo -e "${RED}Generating the private key for the client"
echo
echo -e ${BROWN}${command1}${NC}
${command1}
chmod 400 ${keyfile}

read -p "Press enter to continue "
clear
echo
echo -e "${RED}Generating the CSR for the client"
echo
echo -e ${BROWN}${command2}${NC}
${command2}


read -p "Press enter to continue "
clear
echo
echo -e "${RED}Signing the CSR with the Intermediate CA"
echo
echo -e ${BROWN}${command3}${NC}
${command3}


chmod 444 ${certfile}

read -p "Press enter to continue "
clear
echo
echo -e "${RED}Inspecting the client certificate "
echo
echo -e ${BROWN}${command4}${NC}
${command4}


read -p "Press enter to continue "
clear
echo
echo -e "${RED}Verifying the client certificate"
echo
echo -e ${BROWN}${command5}${NC}
${command5}


