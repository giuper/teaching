#include <stdio.h>
#include <stdlib.h>
#include <rpc/rpc.h>
#include "client.h"

extern int compPerm(physPlainBlock *,physPlainBlock *);
extern int *perm; 
extern clientConf *cf;


void
initServer(serverConf *sc)
{
    physPlainBlock pPB;
	int stat,j;


    stat=callrpc("localhost", ORAMPROG, ORAMVERS, 
        INIT_NUM,
		xdr_serverConf, sc,
		xdr_void, (void *)0);


    if (stat<0){
	    clnt_perrno(stat);
		exit(1);
    }

//upload all blocks to MaxLev

    for(j=0;j<cf->nBlocks;j++){
        pPB.logInd=j;
        pPB.lev=MaxLev;
        if(j<cf->nextDummy){
            sprintf(&(pPB.block),"Block %4d xx",j);
            pPB.dummy=0; 
        }
        else{
            memset(&(pPB.block),'*',sBlock);
            pPB.dummy=1; 
        }
        physWrite(&pPB,MaxLev,j);
    }


    reShuffle();
}



void
initServerOLD(serverConf *sc)
{
    physPlainBlock pPB;
	int stat,j;


    stat=callrpc("localhost", ORAMPROG, ORAMVERS, 
        INIT_NUM,
		xdr_serverConf, sc,
		xdr_void, (void *)0);


    if (stat<0){
	    clnt_perrno(stat);
		exit(1);
    }

//upload all blocks to MaxLev

    for(j=0;j<cf->nBlocks;j++){
        pPB.logInd=j;
        pPB.lev=MaxLev;
        if(j<cf->nextDummy){
            sprintf(&(pPB.block),"Block %4d xx",j);
            pPB.dummy=0; 
        }
        else{
            memset(&(pPB.block),'*',sBlock);
            pPB.dummy=1; 
        }
        physWrite(&pPB,MaxLev,j);
    }


// to be re-written
// pick a random permutation using Fischer Yates 
    fy();
    bSort(0,0,cf->nBits-1,MaxLev,compPerm);  // uses global variable perm*/

/* set up the position map */
    for(j=0;j<cf->nBlocks;j++){
        cf->levPM[j]=MaxLev;
        cf->posPM[j]=perm[j];
    }

}


