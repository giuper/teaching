#include <stdio.h>
#include <stdlib.h>
#include <rpc/rpc.h>
#include "client.h"

extern physPlainBlock **stash;
extern int *levPM, *posPM;
extern int nBits, nBlocks, sStash, rBlocks;
extern int nextStash, nextDummy;
extern int numLogOps;

void
logWrite(char block[sBlock], int id)
{
    

numLogOps++;
    if (numLogOps%sStash==0){
        reShuffle();
        initStash();
    }

    fprintf(stdout,"Log write for block %d found at lev %d and pos %d\n",
                id,levPM[id],posPM[id]);

    if(levPM[id]==0){ //it is in the stash
        memcpy(stash[posPM[id]]->block,block,sBlock);
        physPlainBlock *pb=physRead(1,posPM[nextDummy]);
        physWrite(pb,1,posPM[nextDummy]);
        nextDummy++;
    }
    else{
        physPlainBlock *pb=physRead(1,posPM[id]);
        pb->dummy=2;
        physWrite(pb,1,posPM[id]);
        levPM[id]=0;
        posPM[id]=nextStash++;
        memcpy(stash[posPM[id]]->block,block,sBlock);
        stash[posPM[id]]->lev=0;
        stash[posPM[id]]->logInd=id;
        stash[posPM[id]]->dummy=0;
    }

}
physPlainBlock *
logRead(int id)
{

    physPlainBlock *res, *tmp;

    if(id>=rBlocks) return (physPlainBlock *)0;

numLogOps++;
    if (numLogOps%sStash==0){
        reShuffle();
        initStash();
    }

    if(levPM[id]==0){
        tmp=physRead(1,posPM[nextDummy]);
        physWrite(tmp,1,posPM[nextDummy]);
        nextDummy++;
    }
    
    if(levPM[id]==1){
        tmp=physRead(1,posPM[id]);
        tmp->dummy=2;
        physWrite(tmp,1,posPM[id]);
        stash[nextStash]=tmp;
        stash[nextStash]->lev=0;
        stash[nextStash]->logInd=id;
        stash[nextStash]->dummy=0;
        
        levPM[id]=0;
        posPM[id]=nextStash;

        nextStash++;
    }

    res=(physPlainBlock *)malloc(sizeof(physPlainBlock));
    res->lev=0;
    res->logInd=id;
    res->dummy=0;
    memcpy(&(res->block),stash[posPM[id]]->block,sBlock);

    return res;
    //return stash[posPM[id]];
}

physPlainBlock *
logReadOld(int id)
{

    physPlainBlock *res, *tmp;

    if(id>=rBlocks) return (physPlainBlock *)0;

    //numOps++;
    //if (numOps%sStash==0){
        //reShuffle();
        //initStash();
    //}

    for(int lev=0;lev<=MaxLev;lev++){
        if (lev==levPM[id]){
            res=physRead(lev,posPM[id]);
            if (lev!=0){
                res->dummy=2; physWrite(res,lev,posPM[id]);
                levPM[id]=0;
                posPM[id]=nextStash;
                stash[nextStash++]=res;
                res->lev=0;
                res->logInd=id;
                res->dummy=0;
            }
        }
        else{
            if(lev!=0){
                tmp=physRead(lev,posPM[nextDummy]);
                physWrite(tmp,lev,posPM[nextDummy]);
                nextDummy++;
            }
        }
    }
            
    return res;

}

