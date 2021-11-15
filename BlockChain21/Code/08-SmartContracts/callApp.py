import sys
import json
import base64
from algosdk import account, mnemonic
from algosdk.v2client import algod
from algosdk.future.transaction import write_to_file
from algosdk.future.transaction import ApplicationNoOpTxn
from algosdk.future.transaction import OnComplete
from algosdk.future.transaction import StateSchema
from w4c import wait_for_confirmation

def main():
    if len(sys.argv)!=4:
        print("usage: python3 "+sys.argv[0]+" <mnem> <app index> <node directory>")
        exit()

    MnemFile=sys.argv[1]
    index=int(sys.argv[2])
    directory=sys.argv[3]

    f=open(directory+"/algod.token",'r')
    algodToken=f.read()
    f.close()
    f=open(directory+"/algod.net",'r')
    algodAddress="http://"+f.read()[:-1]   #to remove the trailing newline
    f.close()
    algodClient = algod.AlgodClient(algodToken,algodAddress)

    f=open(MnemFile,'r')
    Mnem=f.read()
    SK=mnemonic.to_private_key(Mnem)
    Addr=account.address_from_private_key(SK)
    f.close()
    params=algodClient.suggested_params()

    utxn=ApplicationNoOpTxn(Addr,params,index)
    write_to_file([utxn],"noop.utxn")
    stxn=utxn.sign(SK)
    write_to_file([stxn],"noop.stxn")
    txId=stxn.transaction.get_txid()
    print("Transaction id: ",txId)
    algodClient.send_transactions([stxn])
    wait_for_confirmation(algodClient,txId,4)
    txResponse=algodClient.pending_transaction_info(txId)
    print("OptIn to app-id: ",txResponse['txn']['txn']['apid'])  

    print("Global values from the TX output")
    if "global-state-delta" in txResponse:
        #print(txResponse['global-state-delta'])
        for variable in txResponse['global-state-delta']:
            key=variable['key']
            key=base64.b64decode(key)
            key=key.decode('utf-8')
            print("Global Key: ",key)
            #print(variable)
            if 'uint' in variable['value']:
                print("Value     : ",variable['value']['uint'])
            else:
                print("Value     : 0")

    print("Local values from the TX output")
    if "local-state-delta" in txResponse :
        #print(txResponse['local-state-delta'])
        for variable in txResponse['local-state-delta'][0]['delta']:
            #key=txResponse['local-state-delta'][0]['delta'][0]['key']
            key=variable['key']
            key=base64.b64decode(key)
            key=key.decode('utf-8')
            print("Local Key : ",key)
            if 'uint' in variable['value']:
                print("Value     : ",variable['value']['uint'])
            else:
                print("Value did not change")

    print("Local values from the user")
    result=algodClient.account_info(Addr)
    localState=result['apps-local-state']
    for st in localState:
        if(st['id']==index):
            for kk in st['key-value']:
                key=kk['key']
                key=base64.b64decode(key)
                key=key.decode('utf-8')
                print("Key    : ",key)
                print("Value  : ",kk['value']['uint'])
        

if __name__=='__main__':
    main()
    
    
