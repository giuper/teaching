#include <stdio.h>
#include <stdlib.h>
#include <rpc/rpc.h>
#include "client.h"

extern clientConf *cf;

#ifdef AAABBB
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
#endif

physPlainBlock *
logRead(int id)
{

    physPlainBlock *res, *tmp;
    int *levPM=cf->levPM;
    int *posPM=cf->posPM;
    int L=cf->maxL;

    if(id>=cf->N+cf->D) return (physPlainBlock *)0;

cf->numLogOps++;

/*
    if (cf->numLogOps%cf->sStash==0){
        reShuffle();
        initStash();
    }
*/

    for(int l=1;l<L;l++){
        if (levPM[id]!=l){
            /* dummy stay dummy */
            tmp=physRead(l,posPM[cf->ND[l]]);
            physWrite(tmp,l,posPM[cf->ND[l]]);
            cf->ND[l]++;
        } else
        {
            tmp=physRead(l,posPM[id]);
            cf->stash[cf->ND[0]]=tmp;
            cf->stash[cf->ND[0]]->lev=0;
            cf->stash[cf->ND[0]]->logInd=id;
            levPM[id]=0;
            posPM[id]=cf->ND[0];
            tmp->state=FILLER;
            physWrite(tmp,l,posPM[cf->ND[l]]);
            tmp->state=REAL;
            cf->ND[0]++;
            cf->r[l]--;
            cf->f[l]++;
        }
    }


    res=(physPlainBlock *)malloc(sizeof(physPlainBlock));
    res->lev=0;
    res->logInd=id;
    res->state=REAL;
    memcpy(&(res->block),cf->stash[posPM[id]]->block,sBlock);
    return res;
}

