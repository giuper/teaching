#!/bin/bash
RED='\033[0;31m'   # Red
BLUE='\033[0;34m'  # Blue
GREEN='\033[0;32m' # Green
BROWN='\033[0;33m' # Brown
NC='\033[0m'       # No Color
BOLD='\033[1m'     # Bold

read -p "Name of recipient: "
client=${REPLY}

keyfile=otherPrivate/${client}.key.pem
certfile=certs/${client}.cert.pem

read -p "Name of document: "
doc=${REPLY}

command1="openssl smime -binary -encrypt -in ${doc} -out ${doc}.cpt ${certfile}"
command2="openssl smime -binary -decrypt -in ${doc}.cpt -recip ${certfile} -inkey ${keyfile} -out ${doc}.new"


echo -e "${RED}Encrypting message ${doc}"
echo
echo -e ${BROWN}${command1}${NC}
${command1}

echo
echo
echo

echo -e "${RED}Decrypting message ${doc}.cpt"
echo
echo -e ${BROWN}${command2}${NC}
${command2}

