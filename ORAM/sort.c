#include <stdio.h>
#include <rpc/rpc.h>
#include "client.h"



extern clientConf *cf;
extern int numOps, totalNumOps;

int *perm; 

void
reversePerm() /* the reverse permutation */
{
    for(int j=0;j<cf->nBlocks;j++) perm[j]=(cf->nBlocks-1)-j;
}

void
fy() /* fischer-yates random perm generation */
{
    int j,rj,tmp;

    int nBlocks=cf->nBlocks;

    perm=(int *)malloc(nBlocks*sizeof(int));

    for(j=0;j<nBlocks;j++) perm[j]=j;
    for(j=0;j<nBlocks-1;j++){
            rj=random()%(nBlocks-j);
            tmp=perm[j]; perm[j]=perm[j+rj]; perm[j+rj]=tmp;
    }
}

int
compPos(physPlainBlock *a, physPlainBlock *b)
{
    return a->pos-b->pos;
}
   



/* dummy come after all non-dummy
*/
   
int
compExcess(physPlainBlock *a, physPlainBlock *b)
{
    int res=a->dummy-b->dummy;
    if ((res==0)&&(a->dummy==0)) res=perm[a->logInd]-perm[b->logInd];
    if ((res==0)&&(a->dummy==1)) res=a->logInd-b->logInd;
    if ((res==0)&&(a->dummy==2)) res=0;
#ifdef DEBUGSORT
    fprintf(stdout,"XXX\t %d %d\tres=%d\n",a->dummy,b->dummy,res);
#endif
    return res;
}
   

int
compPerm(physPlainBlock *a, physPlainBlock *b)
{
    return perm[a->logInd]-perm[b->logInd];
}



void 
rwapGen(int i1, int i2, int lev, int (*aaa)(physPlainBlock *,physPlainBlock *))
{
    int m1=i1;
    int m2=i2;
    
    if (m1>m2){m1=i2;m2=i1;}
/* now we are guaranteed that m1<m2*/

    physPlainBlock *uno=physRead(lev,m1);
    physPlainBlock *due=physRead(lev,m2);
    int res=aaa(uno,due);
#ifdef DEBUGSORT
fprintf(stdout,"XXComparing\n");
fprintf(stdout,"XX\t %d %d\n",m1,uno->dummy);
fprintf(stdout,"XX\t %d %d\n",m2,due->dummy);
fprintf(stdout,"XX\t res=%d\n",res);
#endif
    
    if (res<=0){
        physWrite(uno,lev,m1);
        physWrite(due,lev,m2);
#ifdef DEBUGSORT
        fprintf(stdout,"XX\tNoSwap\n");
#endif
    }
    else{
        physWrite(uno,lev,m2);
        physWrite(due,lev,m1);
#ifdef DEBUGSORT
        fprintf(stdout,"XX\tSwap\n");
#endif
    }
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


