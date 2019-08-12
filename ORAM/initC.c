#include <stdio.h>
#include <stdlib.h>
#include <rpc/rpc.h>
#include "client.h"

extern clientConf *cf;


void
initStash()
{

#ifdef DEBUGINIT
fprintf(stdout,"initStash...");
#endif
    cf->stash=(physPlainBlock *)malloc(cf->sStash*sizeof(physPlainBlock *));
    for(int i=0;i<cf->sStash;i++){
        cf->stash[i]=(physPlainBlock *)0;
    }
    cf->nextStash=0;
    cf->nextDummy=cf->nBlocks-cf->sStash; 
}




void
initClientfromSC(serverConf *sc)
{

    cf            =(clientConf *) malloc(sizeof(clientConf));
    cf->sc        =sc;
    cf->nBits     =(sc->levnBits[MaxLev]);
    cf->nBlocks   =(1<<cf->nBits);
    cf->sStash    =(1<<(sc->levnBits[0])); 
    initStash(cf);
    cf->rBlocks   =cf->nBlocks-cf->sStash;
    cf->levPM     =(int *)malloc(cf->nBlocks*sizeof(int));
    cf->posPM     =(int *)malloc(cf->nBlocks*sizeof(int));
    cf->numPhysOps=0;
    cf->numLogOps =0;

    cf->levSize=(int *)malloc((MaxLev+2)*sizeof(int));
    for(int j=0;j<=MaxLev;j++)
        cf->levSize[j]=(1<<(sc->levnBits[j]));
    cf->levSize[MaxLev+1]=2*cf->levSize[MaxLev];


}


