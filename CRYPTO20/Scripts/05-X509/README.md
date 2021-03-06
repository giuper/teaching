# x509 Certificate Authority #


1. Create the needed directory structure for the Root CA

    Execute [script](setupCA.sh) in the root directory

2. Generate the private key for the Root CA and self-sign it
    to generate the Root CA certificate

    Execute [script](createRootCert.sh) in the root directory

3. Create the needed directory structure for the Intermediate CA

    Execute [script](setupCA.sh) in the intermediate directory

4. Generate the private for the Intermediate CA and produce 
    a CSR for the Root CA

    Execute [script](setupCA.sh) in the intermediate directory

5. Sign the Intermediate CA certificate using the key of the Root CA
    
    Execute [script](signIntermediateCA.sh) in the root directory
    
6. Verify the Intermediate CA certificate

    Execute [script](verifyIntermediate.sh) in the intermediate directory

7. Generate a server certificate signed by the Intermediate CA

    Execute [script](createServer.sh) in the intermediate directory
    
8. Generate a client certificate signed by the Intermediate CA

    Execute [script](createClient.sh) in the intermediate directory
    
## Using Certificates ##

1. Encrypting and Decrypting a document to be sent by email
    
    Execute [script](sMimeEnc.sh) 
             (filenames are relative to the intermediate directory)

2. Signing and Verifying a document to be sent by email

    Execute [script](sMimeSign.sh) 
             (filenames are relative to the intermediate directory)

3. Signing and Encrypting and then Decrypting and Verifying 

    Execute [script](sMimeSignEnc.sh) 
             (filenames are relative to the intermediate directory)

## Config files ##

1. [Config file for the Root CA](opensslRoot.cnf)

2. [Config file for the Intermediate CA](opensslIntermediate.cnf)

