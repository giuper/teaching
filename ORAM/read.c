#include <stdio.h>
#include <stdlib.h>
#include <rpc/rpc.h>
#include <sys/stat.h>
#include <sys/types.h>

#include "client.h"

clientConf *cf;

int
main(int argc, char **argv)
{


physPlainBlock *ppb;

    if (argc<2){
        fprintf(stderr,"Usage: %s <blockID>\n",argv[0]);
        exit(1);
    }
    cf=readClientConf("CLIENT");

    ppb=logRead(atoi(argv[1]));
    printf("Block content for id %4d: %s\n",atoi(argv[1]),ppb->block);
    writeClientConf(cf,"CLIENT");

    printf("numPhysOps=%d\n",cf->numPhysOps);
    printf("numLogOps =%d\n",cf->numLogOps);

}
