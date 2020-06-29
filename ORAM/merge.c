#include <stdio.h>
#include <stdlib.h>
#include <rpc/rpc.h>
#include "client.h"

extern clientConf *cf;

int
comparingBlocks(void *a,void *b)
{

    physPlainBlock **aa=(physPlainBlock **)a;
    physPlainBlock **bb=(physPlainBlock **)b;

    return (*aa)->pos-(*bb)->pos;

}


void
mergeStashIntoOne()
{

    int s0=cf->s[0];
    int s1=cf->s[1];
    int m=s1/s0;
    int tt,r,i,j,t,rj;

#ifdef MERGESTASH
    printf("s0=%4d\ts1=%4d\tm=%4d\n",s0,s1,m);
#endif
    
    physPlainBlock *tmp,*Q[s0][10];
    int nQ[s0];

    int perm[s1];

    for(i=0;i<s1;i++) perm[i]=i;

    for(i=0;i<s0;i++) nQ[i]=0;

    int nb=0;
    for(i=0;i<cf->ND[0];i++){
        tmp=cf->stash[i];
        rj=random()%(s1-nb); 
        tt=perm[nb]; perm[nb]=perm[rj+nb]; perm[rj+nb]=tt;
        tmp->pos=perm[nb]; nb+=1;
        cf->levPM[tmp->logInd]=1;
        cf->posPM[tmp->logInd]=tmp->pos;
        r=tmp->pos/m;
#ifdef MERGESTASH
        printf("D: Block %4d to position %4d queue %4d \n",tmp->logInd,tmp->pos,r);
#endif
        Q[r][nQ[r]]=tmp;
        nQ[r]+=1;
    }
    cf->r[1]+=cf->ND[0];  /* level 1 acquires new real blocks */
    cf->ND[0]=0; /* stash has been emptied */
    

    for(i=0;i<m;i++){
        /*download */
#ifdef MERGESTASH
        printf("Download %d \n",i);
#endif
        for(j=0;j<s0;j++){
            tmp=physRead(1,i*s0+j);
            //printf("reading from 1 %4d state %d\n",i*s0+j,(int)(tmp->state));
            if (tmp->state==FILLER) continue;
            rj=random()%(s1-nb); 
            tt=perm[nb]; perm[nb]=perm[rj+nb]; perm[rj+nb]=tt;
            tmp->pos=perm[nb];nb+=1;
            cf->levPM[tmp->logInd]=1;
            cf->posPM[tmp->logInd]=tmp->pos;
            r=tmp->pos/m;
#ifdef MERGESTASH
            printf("D: Block %4d to position %4d queue %4d \n",tmp->logInd,tmp->pos,r);
#endif
            Q[r][nQ[r]]=tmp;
            nQ[r]+=1;
        }
            
    /* spray */
#ifdef MERGESTASH
        printf("Spray %d \n",i);
#endif
        for(t=0;t<s0;t++){
            if (nQ[t]==0){
                tmp=makeFiller();
#ifdef MERGESTASH
                printf("S: Filler from queue %d in pos %4d\n",t,t*m+i);
#endif
            }
            else {
                tmp=Q[t][nQ[t]-1];
                nQ[t]-=1;
#ifdef MERGESTASH
                printf("S: Block  %4d from queue %d with pos=%4d (%d-%d) goes to %4d\n",tmp->logInd,t,tmp->pos,cf->levPM[tmp->logInd],cf->posPM[tmp->logInd],t*m+i);
#endif
            }
            physWrite(tmp,cf->maxL,t*m+i);
        }
    }

    physPlainBlock *C[m];
    int nC,kk;

    for(i=0;i<s0;i++){
        nC=0;
#ifdef MERGESTASH
        printf("Now I should get blocks from %d to %d\n",i*m,(i+1)*m-1);
#endif
/* the stranded blocks in queue i*/
        for(int j=0;j<nQ[i];j++){
          C[nC]=Q[i][j]; nC+=1;
        }
        
        for(t=0;t<m;t++){
            tmp=physRead(3,i*m+t);
            if (tmp->state==FILLER) continue;
            C[nC]=tmp; nC+=1;
#ifdef MERGESTASH
            printf("%4d(%d)\n",tmp->pos,tmp->logInd);
#endif
        }
        qsort(C,nC,sizeof(physPlainBlock *),comparingBlocks);
#ifdef MERGESTASH
        printf("Now they should be sorted\n");
        for(int kk=0;kk<nC;kk++) printf("%4d\n",C[kk]->pos);
        printf("end\n");
#endif
        kk=0;
        for(t=0;t<m;t++){
            if((kk<nC)&&(C[kk]->pos==i*m+t)){
                tmp=C[kk];
                kk+=1;
#ifdef MERGESTASH
                printf("K: Writing non-filler %4d at %4d (%d)\n",tmp->logInd,tmp->pos,i*m+t);
#endif
            } else {
                tmp=makeFiller();
#ifdef MERGESTASH
                printf("K: Writing a filler at %4d\n",i*m+t);
#endif
            }
            physWrite(tmp,1,i*m+t);
        }
    }
        

    cf->ND[1]=cf->N;
}
