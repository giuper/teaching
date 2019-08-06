#include <stdio.h>
#include <stdlib.h>
#include <rpc/rpc.h>
#include "client.h"

extern physPlainBlock **stash;
extern int *levPM, *posPM;
extern int *perm; /* uhmmm...I do not like it*/
extern int nextStash, nextDummy;

void
logWrite(char block[sBlock], int id)
{
    

    //if (numOps==sStash) reShuffle(0);
    //numOps++; totalNumOps++;

    fprintf(stdout,"Log write for block %d found at lev %d and pos %d\n",
                id,levPM[id],posPM[id]);

    if(levPM[id]==0){ //it is in the stash
        memcpy(stash[posPM[id]]->block,block,sBlock);
        physPlainBlock *pb=physRead(1,perm[nextDummy]);
        physWrite(pb,1,perm[nextDummy++]);
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

    //if (numOps==sStash) reShuffle(0);
    //numOps++; totalNumOps++;

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
                tmp=physRead(lev,perm[nextDummy]);
                physWrite(tmp,lev,perm[nextDummy++]);
            }
        }
    }
            
    return res;

}

