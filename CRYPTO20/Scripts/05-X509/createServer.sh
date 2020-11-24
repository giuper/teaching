#!/bin/bash
RED='\033[0;31m'   # Red
BLUE='\033[0;34m'  # Blue
GREEN='\033[0;32m' # Green
BROWN='\033[0;33m' # Brown
NC='\033[0m'       # No Color
BOLD='\033[1m'     # Bold

read -p "Name of server: "
server=${REPLY}

serverKey=otherPrivate/${server}.key.pem
csrfile=csr/${server}.csr.pem
certfile=certs/${server}.cert.pem
certchain=certs/ca-chain.cert.pem
configFile=./opensslIntermediate.cnf

command1="openssl genrsa -out ${serverKey} 2048"
command2="openssl req -config ${configFile} \
    -key ${serverKey} \
    -new -sha256 -out ${csrfile}"
command3="openssl ca -config ${configFile}\
    -extensions server_cert -days 375 -notext -md sha256\
    -in ${csrfile} \
    -out ${certfile}"
command4="openssl x509 -noout -text -in ${certfile}"
command5="openssl verify -CAfile ${certchain} ${certfile}"


echo -e "${RED}Generating the private key for the server"
echo
echo -e ${BROWN}${command1}${NC}
${command1}
chmod 400 ${serverKey}

read -p "Press enter to continue "
clear
echo
echo -e "${RED}Generating the server's CSR"
echo
echo -e ${BROWN}${command2}${NC}
${command2}

read -p "Press enter to continue "
clear
echo
echo -e "${RED}Signing the CSR with the key of the Intermediate CA"
echo
echo -e ${BROWN}${command3}${NC}
${command3}


chmod 444 ${certfile}

read -p "Press enter to continue "
clear
echo
echo -e "${RED}Inspecting the server's certificate"
echo
echo -e ${BROWN}${command4}${NC}
${command4}


read -p "Press enter to continue "
clear
echo
echo -e "${RED}Verifying the server's certificate"
echo
echo -e ${BROWN}${command5}${NC}
${command5}

