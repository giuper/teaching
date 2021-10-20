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
csr="intermediate/csr/intermediate.csr.pem"
intermediateCert="intermediate/certs/intermediate.cert.pem"
chainCert="intermediate/certs/ca-chain.cert.pem"

command1="openssl ca -config ${configFile} -extensions v3_intermediate_ca \
    -days 3650 -notext -md sha256 \
    -in ${csr} \
    -out ${intermediateCert}"

echo -e "${RED}Signing the CSR: ${csr}"
echo
echo -e ${BROWN}${command1}${NC}
${command1}

chmod 444 ${intermediateCert}

cat ${intermediateCert} ${caCert} > ${chainCert}
chmod 444 ${chainCert}
