#!/bin/bash
RED='\033[0;31m'   # Red
BLUE='\033[0;34m'  # Blue
GREEN='\033[0;32m' # Green
BROWN='\033[0;33m' # Brown
NC='\033[0m'       # No Color
BOLD='\033[1m'     # Bold

moduloLength=2048
privateKeyProtectionAlgo=aes128
hashAlgo=sha256
curve=secp256k1
ECDSAParamFile=dsaparamas.pem
ECDSAPrivateKeyFile=giuperPrivateECDSA.pem
ECDSAPrivateKeyNonArmFile=giuperPrivateECDSANonArm.pem
ECDSAPublicKeyFile=giuperPublicECDSA.pem
plaintext=data.txt
ciphertext=${plaintext}.cpt


#Generating a ECDSA parameters
comando1="openssl genpkey -genparam -algorithm EC -pkeyopt ec_paramgen_curve:${curve} -out ${ECDSAParamFile}"

#Generating a ECDSA private key
comando2="openssl genpkey -${privateKeyProtectionAlgo} -paramfile ${ECDSAParamFile} -out ${ECDSAPrivateKeyFile}"

#Inspecting a ECDSA private key
comando3="openssl pkey -in ${ECDSAPrivateKeyFile} -text -noout"

#Extracting a ECDSA public key
comando4="openssl ec -in ${ECDSAPrivateKeyFile} -out ${ECDSAPublicKeyFile} -pubout"

#Inspecting a ECDSA public key
comando5="openssl pkey -in ${ECDSAPublicKeyFile} -pubin -text -noout"

#Removing the armor
comando6="openssl ec -in ${ECDSAPrivateKeyFile} -out ${ECDSAPrivateKeyNonArmFile}"

#Signing using the ECDSA private key
comando7="openssl dgst -sha256 -sign ${ECDSAPrivateKeyNonArmFile} -out ${plaintext}.sig ${plaintext}"

#Verifying the signature using the ECDSA public key
comando8="openssl dgst -sha256 -verify ${ECDSAPublicKeyFile} -signature ${plaintext}.sig ${plaintext}"


echo -e "${RED}${BOLD}Generating and manipulating ECDSA keys${NC}"


echo -e "${RED}Generating ${moduloLength}-bit ECDSA parameters${NC}"
echo -e "${BLUE}Command: ${GREEN}${comando1}"
echo -e "${BROWN}"
${comando1}
echo -e "${GREEN}"
read -p "Press enter to continue "
echo -e "${NC}"
clear

echo -e "${RED}${BOLD}Generating a ECDSA key private key${NC}"
echo -e "${BLUE}Command: ${GREEN}${comando2}"
${comando2}
echo -e "${GREEN}"
read -p "Press enter to continue "
echo -e "${NC}"
clear


echo -e "${RED}${BOLD}Showing the ECDSA key${NC}"
cat ${ECDSAPrivateKeyFile}
echo -e "${GREEN}"
read -p "Press enter to continue "
echo -e "${NC}"
clear


echo -e "${RED}${BOLD}Inspecting the ECDSA key${NC}"
echo -e "${BLUE}Command:${GREEN} ${comando3}"
echo -e "${BROWN}"
${comando3}
echo -e "${GREEN}"
read -p "Press enter to continue "
echo -e "${NC}"
clear


echo -e "${RED}${BOLD}Storing the ECDSA public key separately${NC}"

echo -e "${BLUE}Command:${GREEN} ${comando4}"
echo -e "${BROWN}"
${comando4}
echo -e "${GREEN}"
read -p "Press enter to continue "
echo -e "${NC}"
clear


echo -e "${RED}${BOLD}Showing the ECDSA public key${NC}"
echo -e "${BLUE}Command: ${GREEN}${comando5}"
echo -e "${BROWN}"
${comando5}
echo -e "${GREEN}"
read -p "Press enter to continue "
clear


echo -e "${RED}${BOLD}Removing the armor from the private key${NC}"
echo -e "${BLUE}Command: ${GREEN}${comando6}"
echo -e "${BROWN}"
${comando6}
echo -e "${GREEN}"
read -p "Press enter to continue "
clear


echo -e "${RED}${BOLD}Randomly selecting a 16-byte AES key ${NC}"
echo -e "${BLUE}Command: ${GREEN}openssl rand -out ${plaintext} 16"
openssl rand -out ${plaintext} 16
echo
echo

echo -e "${RED}${BOLD}Signing the AES key using the ECDSA private key${NC}"
echo -e "${BLUE}Command: ${comando7}"
${comando7}
echo -e "${GREEN}"

echo -e
echo -e
echo -e "${RED}${BOLD}Verifying the signature using the ECDSA public key${NC}"
echo -e "${BLUE}Command: ${comando8}"
echo -e "${BROWN}"
${comando8}
echo -e "${GREEN}"
echo -e 
echo -e

echo -e "${NC}"

