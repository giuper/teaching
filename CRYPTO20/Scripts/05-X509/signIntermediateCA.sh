#!/usr/bin/bash

caKey="private/cakey.pem"
caCert="certs/cacert.pem"
configFile="./opensslRoot.cnf"
csr="intermediate/csr/intermediate.csr.pem"
intermediateCert="intermediate/certs/intermediate.cert.pem"
chainCert="intermediate/certs/ca-chain.cert.pem"

echo "Signing the CSR: ${csr}"
openssl ca -config ${configFile} -extensions v3_intermediate_ca \
    -days 3650 -notext -md sha256 \
    -in ${csr} \
    -out ${intermediateCert}

echo "Certificate found in ${intermediateCert}"

chmod 444 ${intermediateCert}

cat ${intermediateCert} ${caCert} > ${chainCert}
chmod 444 ${chainCert}
