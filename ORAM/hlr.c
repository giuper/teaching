#include <stdio.h>
#include <stdlib.h>
#include <rpc/rpc.h>
#include "client.h"

extern clientConf *cf;

void
logWrite(char block[sBlock], int id)
{
    
int *levPM=cf->levPM;
int *posPM=cf->posPM;
cf->numLogOps++;
    if (cf->numLogOps%cf->sStash==0){
        reShuffle();
        initStash();
    }

    fprintf(stdout,"Log write for block %d found at lev %d and pos %d\n",
                id,levPM[id],posPM[id]);

    if(levPM[id]==0){ //it is in the stash
        memcpy(cf->stash[posPM[id]]->block,block,sBlock);
        physPlainBlock *pb=physRead(1,posPM[cf->nextDummy]);
        physWrite(pb,1,posPM[cf->nextDummy]);
        cf->nextDummy++;
    }
    else{
        physPlainBlock *pb=physRead(1,posPM[id]);
        pb->dummy=2;
        physWrite(pb,1,posPM[id]);
        levPM[id]=0;
        posPM[id]=cf->nextStash++;
        memcpy(cf->stash[posPM[id]]->block,block,sBlock);
        cf->stash[posPM[id]]->lev=0;
        cf->stash[posPM[id]]->logInd=id;
        cf->stash[posPM[id]]->dummy=0;
    }

}

physPlainBlock *
logRead(int id)
{

    physPlainBlock *res, *tmp;
    int *levPM=cf->levPM;
    int *posPM=cf->posPM;

    if(id>=cf->rBlocks) return (physPlainBlock *)0;

cf->numLogOps++;
    if (cf->numLogOps%cf->sStash==0){
        reShuffle();
        initStash();
    }

    if(levPM[id]==0){
        tmp=physRead(1,posPM[cf->nextDummy]);
        physWrite(tmp,1,posPM[cf->nextDummy]);
        cf->nextDummy++;
    }
    
    if(levPM[id]==1){
        tmp=physRead(1,posPM[id]);
        tmp->dummy=2;
        physWrite(tmp,1,posPM[id]);
        cf->stash[cf->nextStash]=tmp;
        cf->stash[cf->nextStash]->lev=0;
        cf->stash[cf->nextStash]->logInd=id;
        cf->stash[cf->nextStash]->dummy=0;
        
        levPM[id]=0;
        posPM[id]=cf->nextStash;

        cf->nextStash++;
    }

    res=(physPlainBlock *)malloc(sizeof(physPlainBlock));
    res->lev=0;
    res->logInd=id;
    res->dummy=0;
    memcpy(&(res->block),cf->stash[posPM[id]]->block,sBlock);

    return res;
    //return stash[posPM[id]];
}

