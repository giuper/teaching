#!/bin/bash
RED='\033[0;31m'   # Red
BLUE='\033[0;34m'  # Blue
GREEN='\033[0;32m' # Green
BROWN='\033[0;33m' # Brown
NC='\033[0m'       # No Color
BOLD='\033[1m'     # Bold


algorithm=aes-256-cbc
plaintext=example.txt
ciphertext=example.cpt
salt=-nosalt
salt=-salt

EncryptionKey="000102030405060708090A0B0C0D0E0F101112131415161718191A1B1C1D1E1F"
IV="AABBCCDDEEFF00112233445566778899"


echo -e "${RED}${BOLD}Encrypting a file using AES${NC}"
echo
echo

##padding adds 0xOF byte until we hit the next multiple of 16



##key derivation described in https://tools.ietf.org/html/rfc2898
##salted by default
##salt is 8 bytes
echo -e "${RED}${BOLD}Encrypting a file using AES cbc with 256-bit key${NC}"
echo -e "${RED}${BOLD}\tKey generated from password and salt${NC}"
echo -e "${BLUE}Encryption command: ${GREEN}openssl enc -${algorithm} ${salt} -in ${plaintext} -out ${ciphertext}${NC}"
echo -e "${BROWN}"
openssl enc -${algorithm} ${salt} -in ${plaintext} -out ${ciphertext}
echo -e "${NC}"
if [ $? -ne 0 ]
then
    echo -e "${BLUE}Error in encryption${NC}"
    exit
else
    :
fi

echo -e "${BLUE}Decryption command: ${GREEN}openssl enc -${algorithm} ${salt} -p -d -in ${ciphertext} -out ${plaintext}.new${NC}"
echo -e "${BROWN}"
openssl enc -${algorithm} ${salt} -p -d  -in ${ciphertext} -out ${plaintext}.new 
echo -e "${NC}"

diff ${plaintext} ${plaintext}.new >/dev/null
if [ $? -eq 0 ]
then
  echo -e "${RED}${BOLD}Successfully decrypted file${NC}"
else
  echo -e "${RED}${BOLD}Error in decryption${NC}"
fi

echo
echo
echo -e "${RED}${BOLD}Encrypting a file using AES cbc with 256-bit key${NC}"
echo -e "${RED}${BOLD}\tKey specified in the command line${NC}"
echo -e "${BLUE}Encryption command: ${GREEN}openssl enc -${algorithm} -K ${EncryptionKey} -iv ${IV} -in ${plaintext} -out ${ciphertext}${NC}"
echo -e "${BROWN}"
openssl enc -${algorithm} -K ${EncryptionKey} -iv ${IV} -in ${plaintext} -out ${ciphertext}
echo -e "${NC}"
if [ $? -ne 0 ]
then
    echo -e "${BLUE}Error in encryption${NC}"
    exit
else
    :
fi
echo -e "${BLUE}Decryption command: ${GREEN}openssl enc -d -${algorithm} -K ${EncryptionKey} -iv ${IV} -in ${ciphertext} -out ${plaintext}.new${NC}"
echo -e "${BROWN}"
openssl enc -d -${algorithm} -K ${EncryptionKey} -iv ${IV} -in ${ciphertext} -out ${plaintext}.new
echo -e "${NC}"
if [ $? -ne 0 ]
then
    echo -e "${BLUE}Error in encryption${NC}"
    exit
else
    :
fi


diff ${plaintext} ${plaintext}.new >/dev/null
if [ $? -eq 0 ]
then
  echo -e "${RED}${BOLD}Successfully decrypted file${NC}"
else
  echo -e "${RED}${BOLD}Error in decryption${NC}"
fi
