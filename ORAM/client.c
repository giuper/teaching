#include <stdio.h>
#include <stdlib.h>
#include <rpc/rpc.h>
#include "go.h"

extern int compExcess(physPlainBlock *a, physPlainBlock *b);
extern int compLogPerm(physPlainBlock *a, physPlainBlock *b);

serverConf sc={1,{2,4,0,0,0,0,0,0,0,0}};

int nBits, nBlocks, sStash;
int nextStash, nextDummy;


int rwapCNT;
physPlainBlock **stash;

int *perm; 
int *levPM, *posPM;
int levSize[MaxNumLev];

int numOps, totalNumOps;

void reShuffle(int);


void
initStash()
{

fprintf(stdout,"initStash...");
    stash=(physPlainBlock *)malloc(sStash*sizeof(physPlainBlock *));
    for(int i=0;i<sStash;i++) stash[i]=(physPlainBlock *)0;
    nextStash=0;
    numOps=0;
fprintf(stdout,"done\n");
}

void
physWrite(physPlainBlock *pPB, int lev,int pI)
{

    static Request *req=(Request *)0;

    if(!req)
        req=(Request *)malloc(sizeof(Request));
    req->lev=lev;
    req->physInd=pI;
    req->logInd=pPB->logInd;
    memcpy(&(req->block),pPB->block,sBlock);

    fprintf(stdout,"writing physical block: %2d (%d) for lev %d\n",req->physInd, req->logInd,req->lev);

	int stat;
    stat=callrpc("localhost", ORAMPROG, ORAMVERS, 
        WRITE_NUM,
		xdr_Request, req,
		xdr_void, (void *)0);

    if (stat<0){
	    clnt_perrno(stat);
		exit(1);
    }


}

/* physRead only gets a phys index and returns physPlainBlock */
physPlainBlock *
physRead(int lev, int physInd)
{

    Request req;

    if (lev==0) return stash[physInd];

	int stat;
    req.lev=lev;
    req.physInd=physInd;
    req.logInd=72;  /* the logInd is ignored by the server */


    fprintf(stdout,"reading physical block: %2d for lev %d\n",req.physInd,req.lev);

    physPlainBlock *res=(physPlainBlock *) malloc(sizeof(physPlainBlock));
    stat=callrpc("localhost", ORAMPROG, ORAMVERS, 
        READ_NUM,
		xdr_Request, &req,
		xdr_physPlainBlock, res);

    if (stat<0){
	    clnt_perrno(stat);
		exit(1);
    }

    return res;

}

void 
sequentialPhysScan()
{
    physPlainBlock *res;
    fprintf(stdout,"Starting a sequential scan\n");
    for(int j=0;j<nBlocks;j++){
        res=physRead(1,j);
        fprintf(stdout,"logical block %2d in physical block %2d-->%c%c\n",res->logInd,j,res->block[0],res->block[1]);
    }
}

#ifdef AAA
void
logWrite(physPlainBlock *pPB)
{
    
    int ptr;
    int found=0;

    if (numOps==sStash) reShuffle(0);
    numOps++; totalNumOps++;

    int logInd=pPB->logInd;
    if(levPM[logInd]!=0){
        levPM[logInd]=0;
        posPM[logInd]=nextStash++;
    }
    pPB->lev=0;
    stash[posPM[logInd]]=pPB;

    for(int lev=1;lev<=MaxLev;lev++)
        physRead(lev,perm[nextDummy++]);
}
#endif

physPlainBlock *
logRead(int logInd)
{

    physPlainBlock *res=(physPlainBlock *)0;
    fprintf(stdout,"Log read for block %d found at lev %d and pos %d\n",logInd,levPM[logInd],posPM[logInd]);
    fprintf(stdout,"\tnextDummy: %d\n",nextDummy);

    //if (numOps==sStash) reShuffle(0);

    numOps++; totalNumOps++;

    for(int lev=0;lev<=MaxLev;lev++){
        if (lev==levPM[logInd]){
            res=physRead(lev,posPM[logInd]);
            if (lev!=0){
                    levPM[logInd]=0;
                    posPM[logInd]=nextStash;
                    stash[nextStash++]=res;
            }
        }
        else
            if(lev!=0) physRead(lev,perm[nextDummy++]);
    }
            
    return res;

}

#ifdef AAA
void
sequentialLogScan()
{
    physPlainBlock *res;

    for(int bn=0;bn<nBlocks;bn++){
        res=logRead(bn);
        //if (res->logInd!=bn){
            fprintf(stdout,"Reading logical block %2d ",bn);
            fprintf(stdout,"logical block %2d read --> %c\n",res->logInd,res->block[0]);
        //}
        //fprintf(stdout,"nextStash=%2d\tnextDummy=%2d\tnumOps=%2d\n",nextStash,nextDummy,numOps);
    }

}
#endif


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


//upload all blocks at the MaxLev

    for(j=0;j<nBlocks;j++){
        pPB.logInd=j;
        pPB.physInd=j; /* do we need this??? */
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
    fprintf(stdout,"\nSorting...\n");
    bSort(0,0,nBits-1,MaxLev,compExcess);  // uses global variable perm*/
    fprintf(stdout,"\n\n");

/* set up the position map */
    for(j=0;j<nBlocks;j++){
        levPM[j]=MaxLev;
        posPM[j]=perm[j];
    }

}



int
main(int argc, char **argv)
{

    physPlainBlock pPB,pPB1, *res;
    int nSOPs;
    nBits     =(sc.levnBits[MaxLev]);
    nBlocks   =(1<<nBits);
    sStash    =(1<<(sc.levnBits[0])); 
    nextDummy=nBlocks/2; /*logical identifier of next unread dummy block*/

    perm=(int *)malloc(nBlocks*sizeof(int));
    levPM=(int *)malloc(nBlocks*sizeof(int));
    posPM=(int *)malloc(nBlocks*sizeof(int));

    fprintf(stdout,"client: starting...\n");
    fprintf(stdout,"\tnBlocks=%4d\n",nBlocks);
    fprintf(stdout,"\tsStash =%4d\n",sStash);
    fprintf(stdout,"client: init...");
    initStash();
    initServer();

    sequentialPhysScan();

    fprintf(stdout,"completed\n");

    res=logRead(0);
    res=logRead(1);
    res=logRead(0);
    res=logRead(3);
    

{
    fprintf(stdout,"Asking to move level 1 to worktape\n");
	int stat;
    int lm=1;
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
   physPlainBlock *dummyB;
    /*fill the empty positions in the stash with dummy blocks*/
   for(i=nextStash;i<sStash;i++){
    dummyB=(physPlainBlock *)malloc(sizeof(physPlainBlock));
    dummyB->dummy=1;
    stash[i]=dummyB;
   }
   for(i=0,pI=nBlocks;i<sStash;i++,pI++) physWrite(stash[i],MaxLev+1,pI);
  }
    
}
    
/*
    totalNumOps=0;
    int stat=callrpc("localhost", ORAMPROG, ORAMVERS, 
        RESET_TELEMETRY_NUM,
		xdr_void, (void *)0,
		xdr_void, (void *)0);
    if (stat<0){
	    clnt_perrno(stat);
		exit(1);
    }

    sequentialPhysScan();
    sequentialLogScan();
*/
    
#ifdef AAAA
   for(int i=0;i<2;i++){
        pPB.logInd=i;
        pPB.block[0]='z';
        logWrite(&pPB);
        pPB1.logInd=i+2;
        pPB1.block[0]='z';
        logWrite(&pPB1);
    }
    sequentialLogScan();

    stat=callrpc("localhost", ORAMPROG, ORAMVERS, 
        READ_TELEMETRY_NUM,
		xdr_void,(void *)0,
		xdr_int, &nSOPs); 
    if (stat<0){
	    clnt_perrno(stat);
		exit(1);
    }

    printf("Log ops: %4d\tPhys ops: %4d\n",totalNumOps,nSOPs);
#endif
    
	exit(0);

}
