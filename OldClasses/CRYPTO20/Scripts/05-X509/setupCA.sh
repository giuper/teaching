#/usr/bin/bash

echo "Preparing the current dir to host a CA"

mkdir certs crl newcerts private csr
chmod 700 private
touch index.txt
echo 1000 > serial
