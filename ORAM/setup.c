#include <stdio.h>
#include <stdlib.h>
#include <rpc/rpc.h>
#include <sys/stat.h>
#include <sys/types.h>

#include "client.h"

serverConf sc={1,{5,10,0,0,0,0,0,0,0,0}};
clientConf *cf;

int
main(int argc, char **argv)
{


    initClientfromSC(&sc);
    initServer(&sc);
    initStash();
    cf->numPhysOps=0;

    physPlainBlock *ppb=logRead(1);
    printf("Block %s\n",ppb->block);
    ppb=logRead(1);
    printf("Block %s\n",ppb->block);
    
    mkdir("CLIENT",0777);
    writeClientConf(cf,"CLIENT");


}
