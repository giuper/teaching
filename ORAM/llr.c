#include <stdio.h>
#include <stdlib.h>
#include <rpc/rpc.h>
#include "client.h"

/* low-level remote client procedures */

extern int compExcess(physPlainBlock *,physPlainBlock *);
extern int compPerm(physPlainBlock *,physPlainBlock *);
extern int compPos(physPlainBlock *,physPlainBlock *);

extern physPlainBlock **stash;
extern int levSize[];
extern int nBits, nBlocks, sStash;
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

    physPlainBlock *res;
	int stat;
    if (lev==0) return stash[physInd];

    rRequest *rr=(rRequest *)malloc(sizeof(rRequest));
    rr->lev=lev;
    rr->physInd=physInd;

#ifdef LOWLEVELDEBUG
    fprintf(stdout,"reading physical block: %2d for lev %d\n",
                rr->physInd,rr->lev);
#endif

    res=(physPlainBlock *) malloc(sizeof(physPlainBlock));
    stat=callrpc("localhost", ORAMPROG, ORAMVERS, 
        READ_NUM,
		xdr_rRequest, rr,
		xdr_physPlainBlock,res);

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
    fprintf(stdout,"\nStarting a sequential scan of level %d\n",lev);
    for(int j=0;j<levSize[lev];j++){
        pPB=physRead(lev,j);
        if(pPB){
        fprintf(stdout,"\tlogical block %4d in physical block %4d (d=%d) pos=%4d \tlevPM=%d\tposPM=%4d: -->%c%c\n",
                pPB->logInd,j,pPB->dummy,pPB->pos,levPM[pPB->logInd],posPM[pPB->logInd],pPB->block[0],pPB->block[1]);
        }
        else {
            fprintf(stdout,"\tlogical block ???? in physical block %4d (d=?) pos=???? \tlevPM=?\tposPM=????: -->??\n",j);
        }
    }
}

void
moveToWorkTape()
{
	int stat;
    int lm=1;

#ifdef LOWLEVELDEBUG
    fprintf(stdout,"Asking to move level 1 to worktape\n");
#endif
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
#ifdef LOWLEVELDEBUG
   fprintf(stdout,"Moving all stash blocks to worktape\n");
#endif
   for(i=0,pI=nBlocks;i<sStash;i++,pI++) physWrite(stash[i],MaxLev+1,pI);
  }
    
}

void
moveFromWorkTape()
{
	int stat;
    int lm=1;

#ifdef LOWLEVELDEBUG
    fprintf(stdout,"Asking to move worktape to level 1\n");
#endif
    stat=callrpc("localhost", ORAMPROG, ORAMVERS, 
        BACK_NUM,
		xdr_int, &lm,
		xdr_void, (void *)0);

    if (stat<0){
	    clnt_perrno(stat);
		exit(1);
    }

    
}



void reShuffle()
{

    int j,tmp,rj,id;
    int perm[nBlocks];
    physPlainBlock *pPB;

    fprintf(stdout,"\n\nReshuffling...\n");


    for(j=0;j<nBlocks;j++) perm[j]=j;

    for(j=0;j<nBlocks;j++){
        rj=random()%(nBlocks-j);
        tmp=perm[j]; perm[j]=perm[j+rj]; perm[j+rj]=tmp;
        pPB=physRead(1,j);
        id=pPB->logInd;
#ifdef LOWLEVELDEBUG
fprintf(stdout,"In phys location %d, we find id %d with status %d\n",j,id,pPB->dummy);
fprintf(stdout,"\tin levPM=%2d\tin posPM=%2d\n",levPM[id],posPM[id]);
fprintf(stdout,"\tgoes to %2d\n",perm[j]);
#endif
        if (pPB->dummy==2){
            if (levPM[id]!=0){
                printf("Error\n");
                exit(1);
            }
            pPB=stash[posPM[id]];

#ifdef LOWLEVELDEBUG
fprintf(stdout,"\tfrom the stash with id %d and status %d\n",pPB->logInd,pPB->dummy);
#endif
        }
        pPB->pos=perm[j];
        levPM[id]=MaxLev;
        posPM[id]=perm[j];
        physWrite(pPB,MaxLev,j);
    }
    bSort(0,0,nBits-1,1,compPos); 
}
