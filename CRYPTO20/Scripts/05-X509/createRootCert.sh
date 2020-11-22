#generating the private key
echo "Generating the private key for the Root CA"
openssl genrsa -aes256 -out private/cakey.pem 4096
chmod 400 private/cakey.pem

echo
echo
echo "Generating a self-signed certificate for the Root CA"
#generating a self-signed certificate
openssl req -config /etc/ssl/openssl.cnf -key private/cakey.pem \
    -new -x509 -days 7300 -sha256 -extensions v3_ca\
    -out certs/cacert.pem
chmod 444 certs/cacert.pem

