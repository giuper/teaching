# x509 Certificate Authority #


1. Step 1: create the needed directory structure for the Root CA

    [script](setupCA.sh)

2. Step 2: generate the private key for the Root CA and self-sign it
    to generate the Root CA certificate

    [script](createRootCert.sh)

3. Step 3: create the needed directory structure for the Intermediate CA

    Execute [script](setupCA.sh) in the intermediate directory

4. Step 4: generate the private for the Intermediate CA and produce 
    a CSR for the Root CA

    Execute [script](setupCA.sh) in the intermediate directory

5. Step 5: sign the Intermediate CA certificate using the key of the Root CA
    
    Execute [script](signIntermediateCA.sh) in the root directory
    
6. Step 6: verify the Intermediate CA certificate
    Execute [script](verifyIntermediate.sh) in the intermediate directory

7. Step 7: generate a server certificate signed by the Intermediate CA
    Execute [script](createServer.sh) in the intermediate directory
    
8. Step 8: generate a client certificate signed by the Intermediate CA
    Execute [script](createClient.sh) in the intermediate directory
    




## Config files ##

1. [Config file for the Root CA](opensslRoot.cnf)

2. [Config file for the Intermediate CA](opensslIntermediate.cnf)

