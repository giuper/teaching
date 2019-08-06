#include <stdio.h>
#include <stdlib.h>
#include <rpc/rpc.h>
#include "client.h"

/* low-level remote client procedures */

extern int compExcess(physPlainBlock *,physPlainBlock *);
extern int compPerm(physPlainBlock *,physPlainBlock *);

extern physPlainBlock **stash;
extern int levSize[];
extern int nBits, nBlocks, sStash;
extern int *perm; 
extern int *levPM, *posPM;

void
physWrite(physPlainBlock *pPB, int lev,int pI)
{

    static wRequest *wr=(wRequest *)0;

    if(!wr)
        wr=(wRequest *)malloc(sizeof(wRequest));
    wr->lev=lev;
    wr->physInd=pI;
    wr->pb=pPB;

#ifdef LOWLEVELDEBUG
    fprintf(stdout,"writing physical block: %2d (%d) for lev %d\n",
            wr->physInd, wr->pb->logInd,wr->lev);
#endif

	int stat;
    stat=callrpc("localhost", ORAMPROG, ORAMVERS, 
        WRITE_NUM,
		xdr_wRequest, wr,
		xdr_void, (void *)0);

    if (stat<0){clnt_perrno(stat);exit(1);}


}

/* physRead only gets a phys index and returns physPlainBlock */
physPlainBlock *
physRead(int lev, int physInd)
{

    static rRequest *rr=(wRequest *)0;

    if (lev==0) return stash[physInd];

    if(!rr)
        rr=(rRequest *)malloc(sizeof(rRequest));

	int stat;
    rr->lev=lev;
    rr->physInd=physInd;

#ifdef LOWLEVELDEBUG
    fprintf(stdout,"reading physical block: %2d for lev %d\n",
                rr->physInd,rr->lev);
#endif

    physPlainBlock *res=(physPlainBlock *) malloc(sizeof(physPlainBlock));
    stat=callrpc("localhost", ORAMPROG, ORAMVERS, 
        READ_NUM,
		xdr_rRequest, rr,
		xdr_physPlainBlock, res);

    if (stat<0){
	    clnt_perrno(stat);
		exit(1);
    }

    return res;

}

void 
sequentialPhysScan(int lev)
{
    physPlainBlock *pPB;
    fprintf(stdout,"Starting a sequential scan of level %d\n",lev);
    for(int j=0;j<levSize[lev];j++){
        pPB=physRead(lev,j);
        fprintf(stdout,"logical block %2d in physical block %2d (%d)-->%c%c\n",
                pPB->logInd,j,pPB->dummy,pPB->block[0],pPB->block[1]);
    }
}

void
moveToWorkTape()
{
	int stat;
    int lm=1;

    fprintf(stdout,"Asking to move level 1 to worktape\n");
    stat=callrpc("localhost", ORAMPROG, ORAMVERS, 
        MOVE_NUM,
		xdr_int, &lm,
		xdr_void, (void *)0);

    if (stat<0){
	    clnt_perrno(stat);
		exit(1);
    }

  {
   int pI,i;
   fprintf(stdout,"Moving all stash blocks to worktape\n");
   for(i=0,pI=nBlocks;i<sStash;i++,pI++) physWrite(stash[i],MaxLev+1,pI);
  }
    
}

void
moveFromWorkTape()
{
	int stat;
    int lm=1;

    fprintf(stdout,"Asking to move worktape to level 1\n");
    stat=callrpc("localhost", ORAMPROG, ORAMVERS, 
        BACK_NUM,
		xdr_int, &lm,
		xdr_void, (void *)0);

    if (stat<0){
	    clnt_perrno(stat);
		exit(1);
    }

    
}



void reShuffle(){
    moveToWorkTape();
fprintf(stdout,"\n\nZZZZ\n");
sequentialPhysScan(MaxLev+1);
fprintf(stdout,"ZZZZ\n\n");
    bSort(0,0,nBits,MaxLev+1,compExcess); 
fprintf(stdout,"\n\nZZZZ\n");
sequentialPhysScan(MaxLev+1);
fprintf(stdout,"ZZZZ\n\n");
    moveFromWorkTape();
    fy();
    for(int j=0;j<nBlocks;j++){
        levPM[j]=MaxLev;
        posPM[j]=perm[j];
    }
    bSort(0,0,nBits-1,MaxLev,compPerm); 
}

