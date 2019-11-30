#!/bin/bash
RED='\033[0;31m'   # Red
BLUE='\033[0;34m'  # Blue
GREEN='\033[0;32m' # Green
BROWN='\033[0;33m' # Brown
NC='\033[0m'       # No Color
BOLD='\033[1m'     # Bold

moduloLength=2048
privateKeyProtectionAlgo=aes128
RSAPrivateKeyFile=giuperPrivateRSA.key
RSAPublicKeyFile=giuperPublicRSA.key
plaintext=aaa.key
ciphertext=${plaintext}.cpt

echo -e "${RED}${BOLD}Generating and manipulating RSA keys${NC}"

echo -e "${RED}Generating a ${moduloLength}-bit RSA key${NC}"
echo -e "${BLUE}Command: ${GREEN}openssl genrsa -${privateKeyProtectionAlgo} -out ${RSAPrivateKeyFile} ${moduloLength}"
echo -e "${BROWN}"
openssl genrsa -${privateKeyProtectionAlgo} -out ${RSAPrivateKeyFile} ${moduloLength}
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

echo -e "${RED}${BOLD}Showing the RSA key${NC}"
echo -e "${BLUE}Command:${GREEN} openssl rsa -text -in ${RSAPrivateKeyFile} -noout"
echo -e "${BROWN}"
openssl rsa -text -in ${RSAPrivateKeyFile} -noout
echo -e "${GREEN}"
read -p "Press enter to continue "
echo -e "${NC}"
clear

echo -e "${RED}${BOLD}Storing the RSA public key separately${NC}"
echo -e "${BLUE}Command:${GREEN} openssl rsa -in ${RSAPrivateKeyFile} -pubout -out ${RSAPublicKeyFile}"
echo -e "${BROWN}"
openssl rsa -in ${RSAPrivateKeyFile} -pubout -out ${RSAPublicKeyFile}
echo -e "${GREEN}"
read -p "Press enter to continue "
echo -e "${NC}"
clear

echo -e "${RED}${BOLD}Showing the RSA public key${NC}"
echo -e "${BLUE}Command: ${GREEN}openssl rsa -pubin -in ${RSAPublicKeyFile} -text -noout"
echo -e "${BROWN}"
openssl rsa -pubin -in ${RSAPublicKeyFile} -text -noout
echo -e "${GREEN}"
read -p "Press enter to continue "
clear

echo -e "${RED}${BOLD}Encrypting the AES key using the RSA public key${NC}"
echo -e "${BLUE}Command: ${GREEN}openssl rsautl -encrypt -oaep -inkey ${RSAPublicKeyFile} -pubin -in ${plaintext} -out ${ciphertext}"
openssl rsautl -encrypt -oaep -inkey ${RSAPublicKeyFile} -pubin -in ${plaintext} -out ${ciphertext}
echo -e "${GREEN}"
read -p "Press enter to continue "

echo -e "${RED}${BOLD}Decrypting the AES key using the RSA public key${NC}"
echo -e "${BLUE}Command: ${GREEN}openssl rsautl -decrypt -oaep -inkey ${RSAPrivateKeyFile} -in ${ciphertext} -out ${plaintext}.new"
openssl rsautl -decrypt -oaep -inkey ${RSAPrivateKeyFile} -in ${ciphertext} -out ${plaintext}.new

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

echo -e "${RED}${BOLD}Signing the AES key using the RSA private key${NC}"
echo -e "${BLUE}Command: ${GREEN}openssl rsautl -sign -inkey ${RSAPrivateKeyFile} -in ${plaintext} -out ${plaintext}.sig"
openssl rsautl -sign -inkey ${RSAPrivateKeyFile} -in ${plaintext} -out ${plaintext}.sig
echo -e "${GREEN}"
read -p "Press enter to continue "

echo -e "${RED}${BOLD}Verifying the signature using the RSA public key${NC}"
echo -e "${BLUE}Command: ${GREEN}openssl rsautl -verify -in ${plaintext}.sig -pubin -inkey ${RSAPublicKeyFile} --out ${plaintext}.vrf"
openssl rsautl -verify -in ${plaintext}.sig -pubin -inkey ${RSAPublicKeyFile} --out ${plaintext}.vrf

diff ${plaintext} ${plaintext}.vrf >/dev/null
if [ $? -eq 0 ]
then
  echo -e "${RED}${BOLD}Successfully verified file${NC}"
else
  echo -e "${RED}${BOLD}Error in verification${NC}"
fi
echo -e "${GREEN}"
read -p "Press enter to continue "
