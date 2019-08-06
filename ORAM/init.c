#include <stdio.h>
#include <stdlib.h>
#include <rpc/rpc.h>
#include "client.h"

extern int compExcess(physPlainBlock *,physPlainBlock *);
extern int compPerm(physPlainBlock *,physPlainBlock *);

extern serverConf sc;
extern int nBits, nBlocks, sStash;
extern int nextStash, nextDummy;
extern physPlainBlock **stash;

extern int *perm; 
extern int *levPM, *posPM;
extern int levSize[MaxNumLev+1];


void
initStash()
{

fprintf(stdout,"initStash...");
    stash=(physPlainBlock *)malloc(sStash*sizeof(physPlainBlock *));
    for(int i=0;i<sStash;i++){
        stash[i]=(physPlainBlock *)malloc(sizeof(physPlainBlock));
        stash[i]->lev=0;
        stash[i]->logInd=2*nBlocks;
        stash[i]->dummy=1;
    }
    nextStash=0;
}



void
initServer()
{
    physPlainBlock pPB;
	int stat,j;

    stat=callrpc("localhost", ORAMPROG, ORAMVERS, 
        INIT_NUM,
		xdr_serverConf, &sc,
		xdr_void, (void *)0);


    if (stat<0){
	    clnt_perrno(stat);
		exit(1);
    }

    for(j=0;j<=MaxLev;j++) levSize[j]=(1<<(sc.levnBits[j]));
    levSize[MaxLev+1]=2*levSize[MaxLev];


//upload all blocks at the MaxLev

    for(j=0;j<nBlocks;j++){
        pPB.logInd=j;
        pPB.lev=MaxLev;
        if(j<nextDummy){
            memset(&(pPB.block),'a'+(j%25),sBlock);
            pPB.dummy=0; 
        }
        else{
            memset(&(pPB.block),'*',sBlock);
            pPB.dummy=1; 
        }
        physWrite(&pPB,MaxLev,j);
    }


// pick a random permutation using Fischer Yates 
    fy();
    bSort(0,0,nBits-1,MaxLev,compPerm);  // uses global variable perm*/

/* set up the position map */
    for(j=0;j<nBlocks;j++){
        levPM[j]=MaxLev;
        posPM[j]=perm[j];
    }

}
