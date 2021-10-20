#!/usr/bin/bash
RED='\033[0;31m'   # Red
BLUE='\033[0;34m'  # Blue
GREEN='\033[0;32m' # Green
BROWN='\033[0;33m' # Brown
NC='\033[0m'       # No Color
BOLD='\033[1m'     # Bold

caKey="private/cakey.pem"
caCert="certs/cacert.pem"
configFile="./opensslRoot.cnf"

command1="openssl genrsa -aes256 -out ${caKey} 4096"
command2="openssl req -config ${configFile} -key ${caKey} \
    -new -x509 -days 7300 -sha256 -extensions v3_ca\
    -out ${caCert}"

echo -e "${RED}Generating the private key for the Root CA"
echo
echo -e ${BROWN}${command1}${NC}
${command1}
chmod 400 ${caKey}
echo
echo

echo -e "${RED}Generating a self-signed certificate for the Root CA"
echo
echo -e ${BROWN}${command2}${NC}
${command2}
chmod 444 ${caCert}

