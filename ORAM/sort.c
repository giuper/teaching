#include <stdio.h>
#include <rpc/rpc.h>
#include "go.h"

extern int nBits, nBlocks, sStash;
extern int nextStash, nextDummy;


extern int rwapCNT;
extern physPlainBlock **stash;

extern int *perm; 
extern int *levPM, *posPM;

extern int numOps, totalNumOps;

void
reversePerm() /* the reverse permutation */
{
    for(int j=0;j<nBlocks;j++) perm[j]=(nBlocks-1)-j;
}

void
fy() /* fischer-yates random perm generation */
{
    int j,rj,tmp;

    for(j=0;j<nBlocks;j++) perm[j]=j;
    for(j=0;j<nBlocks-1;j++){
            rj=random()%(nBlocks-j);
            tmp=perm[j]; perm[j]=perm[j+rj]; perm[j+rj]=tmp;
    }
}



/* dummy come after all non-dummy
*/
   
int
compExcess(physPlainBlock *a, physPlainBlock *b)
{
    int res=a->dummy-b->dummy;
    if (res!=0)
        return res;
    else{
        if (a->dummy==0) return 0;
        else return perm[a->logInd]-perm[b->logInd];
    }
}


int
compLogPerm(physPlainBlock *a, physPlainBlock *b)
{
    int res=perm[a->logInd]-perm[b->logInd];
    if (res!=0) return res; else return a->lev-b->lev;

}

void 
rwapGen(int i1, int i2, int lev, int *cmp(physPlainBlock *,physPlainBlock *))
{
    physPlainBlock *uno=physRead(lev,i1);
    physPlainBlock *due=physRead(lev,i2);
    if (perm[uno->logInd]>perm[due->logInd]){physWrite(uno,lev,i2); physWrite(due,lev,i1);}
    else{physWrite(uno,lev,i1); physWrite(due,lev,i2);}
}

    
void merge(short x, int l, int h, int lev,int *cmp(physPlainBlock *,physPlainBlock *))
{

    if(l==h){
        rwapGen(x|(((short)0)<<l),x|(((short)1)<<l),lev,cmp);
        return;
    }
    merge(x|((short)0)<<l,l+1,h,lev,cmp);
    merge(x|((short)1)<<l,l+1,h,lev,cmp);
    int mx=1<<(h-l+1);
    for(short c=1;c<mx-1;c=c+2){
        rwapGen(x|(c<<l),x|((c+1)<<l),lev,cmp);
    }

}

void
bSort(short x, int l, int h,int lev,int *cmp(physPlainBlock *,physPlainBlock *))
{


    if(l==h){
        rwapGen(x|(((short)0)<<l),x|(((short)1)<<l),lev,cmp);
        return;
    }
        

    bSort(x|((short)0)<<h,l,h-1,lev,cmp);
    bSort(x|((short)1)<<h,l,h-1,lev,cmp);
    merge(x,l,h,lev,cmp);
    return;
}


