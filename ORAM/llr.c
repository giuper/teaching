#include <stdio.h>
#include <stdlib.h>
#include <rpc/rpc.h>
#include "client.h"

/* low-level remote client procedures */


extern clientConf *cf;

void
physWrite(physPlainBlock *pPB, int lev,int pI)
{

cf->numPhysOps++;
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

cf->numPhysOps++;
    physPlainBlock *res;
	int stat;
    if (physInd>cf->levSize[lev]) return (physPlainBlock *)0;

    if (lev==0) return cf->stash[physInd];

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
int *levPM=cf->levPM;
int *posPM=cf->posPM;
physPlainBlock **stash=cf->stash;

    fprintf(stdout,"\nStarting a sequential scan of level %d\n",lev);
    for(int j=0;j<cf->levSize[lev];j++){
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

#ifdef AAA  
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
#endif

int
conf(void *a,void *b)
{

    physPlainBlock **aa=(physPlainBlock **)a;
    physPlainBlock **bb=(physPlainBlock **)b;

    return (*aa)->pos-(*bb)->pos;

}

void
reShuffle()
{

int *levPM=cf->levPM;
int *posPM=cf->posPM;
physPlainBlock **stash=cf->stash;
int sStash=cf->sStash;
int nBlocks=cf->nBlocks;

    int j,tmp,rj,id;
    int r,c,pI,dp;
    int perm[nBlocks];
    physPlainBlock *pPB;
    int dest;

    //fprintf(stdout,"\n\nCacheReshuffling...\n");

    physPlainBlock *cache[sStash][10];
    int nextCache[sStash];
    int nextWork[sStash];

    for(j=0;j<cf->nBlocks;j++) perm[j]=j;

    for(j=0;j<cf->sStash;j++){nextCache[j]=0; nextWork[j]=j*cf->sStash;}

j=0;
    for(r=0;r<cf->nextStash;r++){
        rj=random()%(nBlocks-j);
        tmp=perm[j]; perm[j]=perm[j+rj]; perm[j+rj]=tmp;
        stash[j]->pos=perm[j];
        id=stash[j]->logInd;
        dest=stash[j]->pos/sStash;
        cache[dest][nextCache[dest]]=stash[j];
        levPM[id]=1;
        posPM[id]=perm[j];
        nextCache[dest]++;
        j++;
    }

{int j;
    for(j=0;j<sStash;j++){
        fprintf(stdout,"cache[%d] has %d elements\n",j,nextCache[j]);;
    }
}
    

for(pI=0,r=0;r<sStash;r++){
    for(c=0;c<sStash;c++,pI++){
        pPB=physRead(1,pI);
        if (pPB->dummy==2)
            continue;
        if (!pPB) break;
        id=pPB->logInd;
        rj=random()%(nBlocks-j);
        tmp=perm[j]; perm[j]=perm[j+rj]; perm[j+rj]=tmp;
        pPB->pos=perm[j];
        levPM[id]=1;
        posPM[id]=perm[j];
        dest=pPB->pos/sStash;
        cache[dest][nextCache[dest]]=pPB;
        //printf("Size of cache: %d\n",nextCache[dest]);
        nextCache[dest]++;
        levPM[id]=1;
        posPM[id]=perm[j];
        j++;
    }
    for(int cc=0;cc<sStash;cc++){
        if (nextCache[cc]==0){
            cache[cc][0]=(physPlainBlock *)malloc(sizeof(physPlainBlock));
            cache[cc][0]->dummy=2;
            nextCache[cc]=1;
        }
        nextCache[cc]--;
        physWrite(cache[cc][nextCache[cc]],2,cc*sStash+r);
    }
}


    

#ifdef AAA
{int j;
    for(j=0;j<sStash;j++){
        fprintf(stdout,"\ncache[%d] has %d elements\n",j,nextCache[j]);;
        for(int i=0;i<nextCache[j];i++)
            fprintf(stdout,"\tnextCache[j][i]->logInd=%4d\tnextCache[j][i]->pos=%4d\td=%d\n",
                    cache[j][i]->logInd,
                    cache[j][i]->pos,
                    cache[j][i]->dummy);
    }
}
#endif

//sequentialPhysScan(2);

for(pI=0,r=0;r<sStash;r++){
    cf->nextStash=0;
    for(c=0;c<cf->sStash;c++,pI++){
        pPB=physRead(2,pI);
        if (pPB->dummy==2) continue;
        stash[cf->nextStash++]=pPB;
    }
    for(c=0;c<nextCache[r];c++) stash[cf->nextStash++]=cache[r][c];
    //fprintf(stdout,"\nr=%d\n",r);
    //fprintf(stdout,"Before\n");
    //sequentialPhysScan(0);
    qsort(stash,cf->sStash,sizeof(physPlainBlock *),conf);
    //fprintf(stdout,"After\n");
    //sequentialPhysScan(0);
    for(dp=pI-cf->sStash,c=0;c<cf->sStash;c++,dp++)
        physWrite(stash[c],1,dp);
}
    //initStash();
    //sequentialPhysScan(1);
}

#ifdef LEGACY
extern int compExcess(physPlainBlock *,physPlainBlock *);
extern int compPerm(physPlainBlock *,physPlainBlock *);
extern int compPos(physPlainBlock *,physPlainBlock *);
void reShuffleold()
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
#endif
