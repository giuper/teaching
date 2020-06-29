#include <stdio.h>
#include <stdlib.h>
#include <rpc/rpc.h>
#include "client.h"

serverConf sc={3,{6,9,12,0,0,0,0,0,0,0}};
clientConf *cf;

int
main(int argc, char **argv)
{

    physPlainBlock *res=malloc(sizeof(physPlainBlock));


    initClientfromSC(&sc);

    for(int i=0;i<64;i++){
        res=logRead(i);
        printf("U:%4d %s\n",i,res->block);
    }
    mergeStashIntoOne();

    for(int i=64;i<128;i++){
        res=logRead(i);
        printf("U:%4d %s\n",i,res->block);
    }
    mergeStashIntoOne();

    /* sequentialPhysScan(1);
    sequentialPhysScan(2);
    printf("\n\n");
    */

    for(int i=128;i<192;i++){
        res=logRead(i);
        printf("U:%4d %s\n",i,res->block);
    }
    mergeStashIntoOne();

    for(int i=192;i<256;i++){
        res=logRead(i);
        printf("U:%4d %s\n",i,res->block);
    }
    mergeStashIntoOne();

    for(int i=128;i<192;i++){
        res=logRead(i);
        printf("U:%4d %s\n",i,res->block);
    }
    
    writeClientConf(cf,"CLIENT");
}
