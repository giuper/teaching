#!/bin/bash
RED='\033[0;31m'   # Red
BLUE='\033[0;34m'  # Blue
GREEN='\033[0;32m' # Green
BROWN='\033[0;33m' # Brown
NC='\033[0m'       # No Color
BOLD='\033[1m'     # Bold

cafile=certs/ca-chain.cert.pem

read -p "Name of recipient: "
recipient=${REPLY}
rkeyfile=otherPrivate/${recipient}.key.pem
rcertfile=certs/${recipient}.cert.pem

read -p "Name of sender:    "
sender=${REPLY}
skeyfile=otherPrivate/${sender}.key.pem
scertfile=certs/${sender}.cert.pem

read -p "Name of document:  "
doc=${REPLY}
signedDoc=${doc}.sig
encSignedDoc=${doc}.sig.cpt
decSignedDoc=${doc}.sig.new
verifiedDoc=${doc}.new


command1="openssl smime -sign -in ${doc} -out ${signedDoc}\
    -signer ${scertfile}\
    -inkey ${skeyfile} -text"

command2="openssl smime -binary -encrypt -in ${signedDoc}\
    -out  ${encSignedDoc} ${rcertfile}"

command3="openssl smime -binary -decrypt -in ${encSignedDoc}\
    -recip ${rcertfile} -inkey ${rkeyfile} -out ${decSignedDoc}"

command4="openssl smime -verify -text -CAfile ${cafile}\
    -in ${decSignedDoc} -out ${verifiedDoc}"

echo -e "${RED}1. sign message ${doc} using ${sender}'s private key"
echo
echo -e ${BROWN}${command1}${NC}
${command1}
if [ $? -ne 0 ]; then
    echo "Error"
    exit 1
fi
echo
echo


echo -e "${RED}2. encrypt signed message ${signedDoc} with ${recipient}'s public key"
echo
echo -e ${BROWN}${command2}${NC}
${command2}
if [ $? -ne 0 ]; then
    echo "Error"
    exit 1
fi
echo
echo


echo -e "${RED}3. decrypt ciphertext  ${encSignedDoc} using ${recipient}'s private key"
echo
echo -e ${BROWN}${command3}${NC}
${command3}

if [ $? -ne 0 ]; then
    echo "Error"
    exit 1
fi
echo
echo

echo -e "${RED}4. verify the decypted signed doc ${decSignedDoc}"
echo
echo -e ${BROWN}${command4}${NC}
echo -e ${GREEN}
${command4}
echo -e ${NC}

if [ $? -ne 0 ]; then
    echo "Error"
    exit
fi
echo
echo

