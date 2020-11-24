#!/usr/bin/bash
RED='\033[0;31m'   # Red
BLUE='\033[0;34m'  # Blue
GREEN='\033[0;32m' # Green
BROWN='\033[0;33m' # Brown
NC='\033[0m'       # No Color
BOLD='\033[1m'     # Bold

caKey="private/intermediate.key.pem"
csr="csr/intermediate.csr.pem"
configFile="./opensslIntermediate.cnf"

command1="openssl genrsa -aes256 -out ${caKey} 4096"
command2="openssl req -config ${configFile} -new -sha256 \
    -key ${caKey}\
    -out ${csr}"

echo -e "${RED}Generating the private key for the Intermediate CA"
echo
echo -e ${BROWN}${command1}${NC}
${command1}
chmod 400 ${caKey}

echo
echo
echo -e "${RED}Generating a CSR for the Intermediate CA"
echo
echo -e ${BROWN}${command2}${NC}
${command2}

