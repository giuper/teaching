#include <stdio.h>
#include <stdlib.h>
#include <rpc/rpc.h>
#include "client.h"

extern clientConf *cf;


void
initStash()
{

#ifdef INITSTASH
fprintf(stdout,"initStash...");
#endif

    cf->stash=(physPlainBlock *)malloc(cf->n[0]*sizeof(physPlainBlock *));
    for(int i=0;i<cf->n[0];i++) cf->stash[i]=(physPlainBlock *)0;

#ifdef INITSTASH
fprintf(stdout,"\n\tsize of stash\t%d\n",cf->n[0]);
fprintf(stdout,"\n\tnext stash\t%d\n",cf->NStash);
#endif
}


physPlainBlock *
makeReal(int lev, int logInd)
{

    physPlainBlock *pb = (physPlainBlock *)malloc(sizeof(physPlainBlock));
    pb->lev            = lev;
    pb->logInd         = logInd;
    pb->state          = REAL;
    sprintf(pb->block,"Real  block %5d ***",logInd);

    return pb;
}

physPlainBlock *
makeDummy(int lev, int logInd)
{

    physPlainBlock *pb = (physPlainBlock *)malloc(sizeof(physPlainBlock));
    pb->lev            = lev;
    pb->logInd         = logInd;
    pb->state          = DUMMY;
    sprintf(pb->block,"Dummy block %5d ***",logInd);

    return pb;
}

physPlainBlock *
makeFiller()
{

    physPlainBlock *pb = (physPlainBlock *)malloc(sizeof(physPlainBlock));
    pb->lev            = -1;
    pb->logInd         = -1;
    pb->state          = FILLER;
    sprintf(pb->block,"FIller ***");

    return pb;
}

void
fillLastLevel()
{

    int L=cf->maxL-1;   /* index of the last level */
    int S=cf->s[L];     /* size of the last level */
    int R=cf->r[L];     /* number of reals of the last level */

    /* construct a random permutation of the last level */
    int perm[S];
    for (int i=0;i<S;i++) perm[i]=i;
    int ri, temp;
    physPlainBlock *pb;
    for (int i=0;i<S-1;i++){
        ri=random()%(S-i);
        temp=perm[i]; perm[i]=perm[i+ri]; perm[i+ri]=temp;
        if (perm[i]<R){
        /* real block perm[i] goes to physical position i in last level */
            pb=makeReal(L,perm[i]);
            cf->levPM[perm[i]]=L;
            cf->posPM[perm[i]]=i;
        }
        else{
        /* dummy block (cf->ND[L]-cf->n[L])+perm[i] goes to physical position i in last level */
            pb=makeDummy(L,(cf->ND[L]-cf->n[L])+perm[i]);
            cf->levPM[(cf->ND[L]-cf->n[L])+perm[i]]=L;
            cf->posPM[(cf->ND[L]-cf->n[L])+perm[i]]=i;
        }
        if(physWrite(pb,L,i)==-25){fprintf(stderr,"Write failed\n");}
    }

    if (perm[S-1]<R){
        pb=makeReal(L,perm[S-1]);
        cf->levPM[perm[S-1]]=L;
        cf->posPM[perm[S-1]]=S-1;
    }
    else{
        pb=makeDummy(L,(cf->ND[L]-cf->n[L])+perm[S-1]);
        cf->levPM[(cf->ND[L]-cf->n[L])+perm[S-1]]=L;
        cf->posPM[(cf->ND[L]-cf->n[L])+perm[S-1]]=S-1;
    }
    physWrite(pb,L,S-1);
        
}

/* reals are only in the last level
   the other levels contain fillers and dummy only */

void 
fillLevel(int level)
{

    int S=cf->s[level]; /* size of the level being built*/
    int D=cf->d[level]; /* number of dummy in the level */

#ifdef ICFSC
    printf("FL: filling level %d of size %d with %d dummy block\n", 
                level,S,D);
    printf("FL: dummy go from %d to %d\n",cf->ND[level],cf->ND[level]+D-1);
#endif

    /* construct a random permutation of the blocks of the level */
    int perm[S];
    for (int i=0;i<S;i++) perm[i]=i;
    int ri, temp;
    physPlainBlock *pb;

    for (int i=0;i<S-1;i++){
        ri=random()%(S-i);
        temp=perm[i]; perm[i]=perm[i+ri]; perm[i+ri]=temp;
        if (perm[i]<D){
            pb=makeDummy(level,cf->ND[level]+perm[i]);
            cf->levPM[cf->ND[level]+perm[i]]=level;
            cf->posPM[cf->ND[level]+perm[i]]=i;
#ifdef ICFSC
            printf("FL: dummy %d goes to pos %d in level %d\n",
                cf->ND[level]+perm[i],i,level);
#endif
        }
        else
            pb=makeFiller();
        physWrite(pb,level,i);
    }
    if (perm[S-1]<D){
        pb=makeDummy(level,cf->ND[level]+perm[S-1]);
        cf->levPM[cf->ND[level]+perm[S-1]]=level;
        cf->posPM[cf->ND[level]+perm[S-1]]=S-1;
    }
    else
        pb=makeFiller();
    physWrite(pb,level,S-1);

}



void
initClientfromSC(serverConf *sc)
{

    serverSetup ss;

    cf            =(clientConf *) malloc(sizeof(clientConf));
    cf->sc        =sc;
    int maxL      =sc->maxL;
    cf->maxL      =sc->maxL;

    cf->N         =(1<<(sc->nb[maxL-1]));
    cf->D         =0;
    cf->n         =(int *)malloc(maxL*sizeof(int));
    cf->r         =(int *)malloc(maxL*sizeof(int));
    cf->f         =(int *)malloc(maxL*sizeof(int));
    cf->d         =(int *)malloc(maxL*sizeof(int));
    cf->s         =(int *)malloc((maxL+1)*sizeof(int));
    cf->ND        =(int *)malloc(maxL*sizeof(int));

    cf->n[0]=(1<<(sc->nb[0]));
    cf->r[0]=0; cf->f[0]=cf->n[0];
    cf->d[0]=0;
    cf->s[0]=cf->n[0];
    cf->ND[0]=0; /* previously known as nextStash */

    for (int l=1;l<maxL-1;l++){
        cf->n[l]=(1<<(sc->nb[l]));
        cf->r[l]=0; cf->f[l]=cf->n[l];
        cf->d[l]=cf->s[l-1];
        cf->s[l]=cf->r[l]+cf->f[l]+cf->d[l];
        cf->ND[l]=cf->N+cf->D;
        cf->D+=cf->d[l];
    }

    cf->n[maxL-1]=(1<<(sc->nb[maxL-1]));
    cf->r[maxL-1]=cf->n[maxL-1]; cf->f[maxL-1]=0;
    cf->d[maxL-1]=cf->s[maxL-2];
    cf->s[maxL-1]=cf->r[maxL-1]+cf->f[maxL-1]+cf->d[maxL-1];
    cf->ND[maxL-1]=cf->N+cf->D;
    cf->D+=cf->d[maxL-1];
    cf->s[maxL]=cf->s[maxL-1];
    initStash(cf);

    cf->levPM     =(int *)malloc((cf->D+cf->N)*sizeof(int));
    cf->posPM     =(int *)malloc((cf->D+cf->N)*sizeof(int));
    cf->numPhysOps=0;
    cf->numLogOps =0;

#ifdef ICFSC
fprintf(stdout,"Client initialization for %d real blocks\n",cf->N);
for(int l=0;l<maxL;l++){
        printf("%d\tn:  %4d\n",l,cf->n[l]);
        printf("%d\tr:  %4d\n",l,cf->r[l]);
        printf("%d\tf:  %4d\n",l,cf->f[l]);
        printf("%d\td:  %4d\n",l,cf->d[l]);
        printf("%d\ts:  %4d\n",l,cf->s[l]);
        printf("%d\tND: %4d\n",l,cf->ND[l]);
}
        printf("\n\tD: %d\n",cf->D);
#endif

    ss.maxL=cf->maxL;
    for(int l=1;l<maxL;l++) ss.s[l]=cf->s[l];

    fprintf(stdout,"calling...\n");
    int stat=callrpc("localhost",ORAMPROG,ORAMVERS,
        BUILDLEV_NUM,
        xdr_serverSetup, (char *) &ss,
        xdr_void, (char *) 0);
    if (stat!=0){
        clnt_perrno(stat);
        fprintf(stderr,"\n");
        exit(1);
    }
    fprintf(stdout,"no error...\n");
    

    fillLastLevel();
    for(int l=1;l<cf->maxL-1;l++) fillLevel(l);


}


