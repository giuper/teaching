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
DSAParamFile=dsaparamas.pem
DSAPrivateKeyFile=giuperPrivateDSA.pem
DSAPrivateKeyNonArmFile=giuperPrivateDSANonArm.pem
DSAPublicKeyFile=giuperPublicDSA.pem
plaintext=aaa.key
ciphertext=${plaintext}.cpt

#Generating a DSA parameters
comando1="openssl genpkey -genparam -algorithm DSA -pkeyopt dsa_paramgen_bits:${moduloLength} -pkeyopt dsa_paramgen_q_bits:256 -pkeyopt dsa_paramgen_md:${hashAlgo} -out ${DSAParamFile}"

#Generating a DSA private key
comando2="openssl genpkey -${privateKeyProtectionAlgo} -paramfile ${DSAParamFile} -out ${DSAPrivateKeyFile}"

#Inspecting a DSA private key
comando3="openssl pkey -in ${DSAPrivateKeyFile} -text -noout"

#Extracting a DSA public key
comando4="openssl dsa -in ${DSAPrivateKeyFile} -out ${DSAPublicKeyFile} -pubout"

#Inspecting a DSA public key
comando5="openssl pkey -in ${DSAPublicKeyFile} -pubin -text -noout"

#Removing the armor
comando6="openssl dsa -in ${DSAPrivateKeyFile} -out ${DSAPrivateKeyNonArmFile}"

#Signing using the DSA private key
comando7="openssl dgst -sha256 -sign ${DSAPrivateKeyNonArmFile} -out ${plaintext}.sig ${plaintext}"

#Verifying the signature using the DSA public key
comando8="openssl dgst -sha256 -verify ${DSAPublicKeyFile} -signature ${plaintext}.sig ${plaintext}"


echo -e "${RED}${BOLD}Generating and manipulating DSA keys${NC}"


echo -e "${RED}Generating ${moduloLength}-bit DSA parameters${NC}"
echo -e "${BLUE}Command: ${GREEN}${comando1}"
echo -e "${BROWN}"
${comando1}
echo -e "${GREEN}"
read -p "Press enter to continue "
echo -e "${NC}"
clear

echo -e "${RED}${BOLD}Generating a DSA key private key${NC}"
echo -e "${BLUE}Command: ${GREEN}${comando2}"
${comando2}
echo -e "${GREEN}"
read -p "Press enter to continue "
echo -e "${NC}"
clear


echo -e "${RED}${BOLD}Showing the DSA key${NC}"
cat ${DSAPrivateKeyFile}
echo -e "${GREEN}"
read -p "Press enter to continue "
echo -e "${NC}"
clear


echo -e "${RED}${BOLD}Inspecting the DSA key${NC}"
echo -e "${BLUE}Command:${GREEN} ${comando3}"
echo -e "${BROWN}"
${comando3}
echo -e "${GREEN}"
read -p "Press enter to continue "
echo -e "${NC}"
clear


echo -e "${RED}${BOLD}Storing the DSA public key separately${NC}"

echo -e "${BLUE}Command:${GREEN} ${comando4}"
echo -e "${BROWN}"
${comando4}
echo -e "${GREEN}"
read -p "Press enter to continue "
echo -e "${NC}"
clear


echo -e "${RED}${BOLD}Showing the DSA public key${NC}"
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

echo -e "${RED}${BOLD}Signing the AES key using the DSA private key${NC}"
echo -e "${BLUE}Command: ${comando7}"
${comando7}
echo -e "${GREEN}"

echo -e
echo -e
echo -e "${RED}${BOLD}Verifying the signature using the DSA public key${NC}"
echo -e "${BLUE}Command: ${comando8}"
echo -e "${BROWN}"
${comando8}
echo -e "${GREEN}"
echo -e 
echo -e

echo -e "${NC}"

