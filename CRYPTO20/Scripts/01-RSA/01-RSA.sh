#!/bin/bash
RED='\033[0;31m'   # Red
BLUE='\033[0;34m'  # Blue
GREEN='\033[0;32m' # Green
BROWN='\033[0;33m' # Brown
NC='\033[0m'       # No Color
BOLD='\033[1m'     # Bold

moduloLength=2048
privateKeyProtectionAlgo=aes128
RSAPrivateKeyFile=giuperPrivateRSA.pem
RSAPrivateKeyNonArmFile=giuperPrivateRSANonArm.pem
RSAPublicKeyFile=giuperPublicRSA.pem
plaintext=aaa.key
ciphertext=${plaintext}.cpt

#generating the private key
comando1="openssl genpkey -${privateKeyProtectionAlgo} -algorithm RSA -pkeyopt rsa_keygen_bits:${moduloLength} -out ${RSAPrivateKeyFile}"


#inspecting the private key
comando2="openssl pkey -in ${RSAPrivateKeyFile} -text -noout"

#extracting the public key
comando3="openssl pkey -in ${RSAPrivateKeyFile} -out ${RSAPublicKeyFile} -pubout"

#inspecting the publick key
comando4="openssl pkey -in ${RSAPublicKeyFile} -pubin -text -noout"

#removing the armor
comando5="openssl rsa -in ${RSAPrivateKeyFile} -out ${RSAPrivateKeyNonArmFile}"

#generating randomness
comando6="openssl rand -out ${plaintext} 16"

#encrypting using the public key
comando7="openssl rsautl -encrypt -oaep -pubin -inkey ${RSAPublicKeyFile} -in ${plaintext} -out ${ciphertext}"

#decrypting using the private key
comando8="openssl rsautl -decrypt -oaep -inkey ${RSAPrivateKeyFile} -in ${ciphertext} -out ${plaintext}.new"

#signing using the private key (obsolete)
comando9="openssl rsautl -sign -inkey ${RSAPrivateKeyFile} -in ${plaintext} -out ${plaintext}.sig"

#verifying using the public key (obsolete)
comando10="openssl rsautl -verify -pubin -inkey ${RSAPublicKeyFile} -in ${plaintext}.sig -out ${plaintext}.vrf"

#signing using the private key 
comando11="openssl dgst -sha256 -sign ${RSAPrivateKeyFile} -out ${plaintext}.sig ${plaintext}"

#verifying using the public key
comando12="openssl dgst -sha256 -verify ${RSAPublicKeyFile} -signature ${plaintext}.sig ${plaintext}"
echo -e "${RED}${BOLD}Generating and manipulating RSA keys${NC}"

echo -e "${RED}Generating a ${moduloLength}-bit RSA key${NC}"
echo -e "${BLUE}Command: ${GREEN}${comando1}"
echo -e "${BROWN}"
${comando1}
echo -e "${GREEN}"
read -p "Press enter to continue "
echo -e "${NC}"
clear

echo -e "${RED}${BOLD}Showing the RSA key${NC}"
cat ${RSAPrivateKeyFile}
echo -e "${GREEN}"
read -p "Press enter to continue "
echo -e "${NC}"
clear

##Obsolete
##echo -e "${RED}${BOLD}Showing the RSA key${NC}"
##echo -e "${BLUE}Command:${GREEN} openssl rsa -text -in ${RSAPrivateKeyFile} -noout"
##echo -e "${BROWN}"
##openssl rsa -text -in ${RSAPrivateKeyFile} -noout
##echo -e "${GREEN}"
##read -p "Press enter to continue "
##echo -e "${NC}"
##clear

echo -e "${RED}${BOLD}Showing the RSA key${NC}"
echo -e "${BLUE}Command: ${GREEN}${comando2}"
echo -e "${BROWN}"
${comando2}
echo -e "${GREEN}"
read -p "Press enter to continue "
echo -e "${NC}"
clear

##Obsolete
##echo -e "${RED}${BOLD}Storing the RSA public key separately${NC}"
##echo -e "${BLUE}Command:${GREEN} openssl rsa -pubout -in ${RSAPrivateKeyFile} -out ${RSAPublicKeyFile}"
##echo -e "${BROWN}"
##openssl rsa -pubout -in ${RSAPrivateKeyFile} -out ${RSAPublicKeyFile} 
##echo -e "${GREEN}"
##read -p "Press enter to continue "
##echo -e "${NC}"
##clear

echo -e "${RED}${BOLD}Storing the RSA public key separately${NC}"
echo -e "${BLUE}Command: ${GREEN}${comando3}"
echo -e "${BROWN}"
${comando3}
echo -e "${GREEN}"
read -p "Press enter to continue "
echo -e "${NC}"
clear

##Obsolete
##echo -e "${RED}${BOLD}Showing the RSA public key${NC}"
##echo -e "${BLUE}Command: ${GREEN}openssl rsa -pubin -in ${RSAPublicKeyFile} -text -noout"
##echo -e "${BROWN}"
##openssl rsa -pubin -in ${RSAPublicKeyFile} -text -noout
##echo -e "${GREEN}"
##read -p "Press enter to continue "
##clear

echo -e "${RED}${BOLD}Showing the RSA public key${NC}"
echo -e "${BLUE}Command: ${GREEN}${comando4}"
echo -e "${BROWN}"
${comando4}
echo -e "${GREEN}"
read -p "Press enter to continue "
clear

echo -e "${RED}${BOLD}Removing the armor from the private key${NC}"
echo -e "${BLUE}Command: ${GREEN}${comando5}"
echo -e "${BROWN}"
${comando5}
echo -e "${GREEN}"
read -p "Press enter to continue "
clear

echo -e "${RED}${BOLD}Randomly selecting a 16-byte AES key ${NC}"
echo -e "${BLUE}Command: ${GREEN}${comando6}"
${comando6}
echo
echo

echo -e "${RED}${BOLD}Encrypting the AES key using the RSA public key${NC}"
echo -e "${BLUE}Command: ${GREEN}${comando7}"
${comando7}
echo -e "${GREEN}"
read -p "Press enter to continue "

echo -e
echo -e
echo -e "${RED}${BOLD}Decrypting the AES key using the RSA private key${NC}"
echo -e "${BLUE}Command: ${GREEN}${comando8}"
${comando8}

diff ${plaintext} ${plaintext}.new >/dev/null
if [ $? -eq 0 ]
then
  echo -e "${RED}${BOLD}Successfully decrypted file${NC}"
else
  echo -e "${RED}${BOLD}Error in decryption${NC}"
fi
echo -e "${GREEN}"
read -p "Press enter to continue "
clear

echo -e "${RED}${BOLD}Signing the AES key using the RSA private key (obsolete)${NC}"
echo -e "${BLUE}Command: ${GREEN}${comando9}"
${comando9}
echo -e "${GREEN}"
read -p "Press enter to continue "

echo -e
echo -e
echo -e "${RED}${BOLD}Verifying the signature using the RSA public key (obsolete)${NC}"
echo -e "${BLUE}Command: ${GREEN}${comando10}"
${comando10}

diff ${plaintext} ${plaintext}.vrf >/dev/null
if [ $? -eq 0 ]
then
  echo -e "${RED}${BOLD}Successfully verified file${NC}"
else
  echo -e "${RED}${BOLD}Error in verification${NC}"
fi
echo -e "${GREEN}"
read -p "Press enter to continue "

clear
echo -e "${RED}${BOLD}Signing the AES key using the RSA private key${NC}"
echo -e "${BLUE}Command: ${GREEN}${comando11}"
${comando11}
echo -e "${GREEN}"
read -p "Press enter to continue "

echo -e
echo -e
echo -e "${RED}${BOLD}Verifying the signature using the RSA public key${NC}"
echo -e "${BLUE}Command: ${GREEN}${comando12}"
${comando12}
echo -e 
echo -e

echo -e "${NC}"

