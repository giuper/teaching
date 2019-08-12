#include <stdio.h>
#include <stdlib.h>

#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

#include <rpc/rpc.h>
#include "client.h"

void
writePM(FILE *fd, int *a, int len)
{

    int i;

    fprintf(fd,"%d\n",len);
    for(i=0;i<len;i++){
        fprintf(fd,"%d\n",a[i]);
    }

}


void
writeSC(FILE *fd,serverConf *sc)
{
    int i;

    fprintf(fd,"%d\n",sc->numLev);
    for(i=0;i<=sc->numLev;i++)
        fprintf(fd,"%d\n",sc->levnBits[i]);

}

void
writeStash(clientConf *cf, char *dirname)
{

    int i,fd;
    FILE *ffd;
    char filename[100];

    //printf("nextStash=%d\n",cf->nextStash);
    for(i=0;i<cf->nextStash;i++){
        sprintf(filename,"%s/Block%d.pos",dirname,i);
        ffd=fopen(filename,"w");
        fprintf(ffd,"%d\n",cf->stash[i]->logInd);
        fclose(ffd);

        sprintf(filename,"%s/Block%d.cnt",dirname,i);
        fd=open(filename,O_WRONLY|O_CREAT,S_IRUSR|S_IWUSR);
        write(fd,cf->stash[i]->block,sBlock);
        close(fd);
    }
}

void
writeClientConf(clientConf *cf, char *dirname)
{

    char filename[1000];
    char stashDIR[1000];
    FILE *fd;

    mkdir(dirname,0777);

    sprintf(filename,"%s/Nops.cnf",dirname);
    fd=fopen(filename,"w");
    fprintf(fd,"%d\n",cf->numPhysOps);
    fprintf(fd,"%d\n",cf->numLogOps);
    fclose(fd);

    sprintf(filename,"%s/SC.cnf",dirname);
    fd=fopen(filename,"w");
    writeSC(fd,cf->sc);
    fclose(fd);
    
    sprintf(filename,"%s/ND.cnf",dirname);
    fd=fopen(filename,"w");
    fprintf(fd,"%d\n",cf->nextDummy);
    fclose(fd);
    
    sprintf(filename,"%s/NS.cnf",dirname);
    fd=fopen(filename,"w");
    fprintf(fd,"%d\n",cf->nextStash);
    fclose(fd);
    
    sprintf(filename,"%s/levPM.cnf",dirname);
    fd=fopen(filename,"w");
    writePM(fd,cf->levPM,cf->nBlocks);
    fclose(fd);
    
    sprintf(filename,"%s/posPM.cnf",dirname);
    fd=fopen(filename,"w");
    writePM(fd,cf->posPM,cf->nBlocks);
    fclose(fd);
    
    sprintf(stashDIR,"%s/STASH",dirname);
    mkdir(stashDIR,0777);
    writeStash(cf,stashDIR);
}


physPlainBlock **
readStash(clientConf *cf, char *dirname)
{

    int i,fd;
    FILE *ffd;
    char filename[100];
    physPlainBlock **stash=(physPlainBlock **)malloc(cf->sStash*sizeof(physPlainBlock));

    //printf("nextStash=%d\n",cf->nextStash);
    for(i=0;i<cf->nextStash;i++){
        stash[i]=(physPlainBlock *)malloc(sizeof(physPlainBlock));
        sprintf(filename,"%s/Block%d.pos",dirname,i);
        ffd=fopen(filename,"r");
        fscanf(ffd,"%d",&(stash[i]->logInd));
        fclose(ffd);

        sprintf(filename,"%s/Block%d.cnt",dirname,i);
        fd=open(filename,O_RDONLY);
        read(fd,stash[i]->block,sBlock);
        close(fd);
        stash[i]->lev=0;
        stash[i]->dummy=0;
    }
    for(i=cf->nextStash;i<cf->sStash;i++)
        stash[i]=(physPlainBlock *)0;

    return stash;

}

int *
readPM(FILE *fd)
{

    int i;
    int len;
    int *pm;

    fscanf(fd,"%d",&len);
    pm=(int *)malloc(len*sizeof(int));
    
    for(i=0;i<len;i++) fscanf(fd,"%d",pm+i);
    return pm;

}

serverConf *
readSC(FILE *fd)
{
    int i;

    serverConf *sc=(serverConf *)malloc(sizeof(serverConf));

    fscanf(fd,"%d",&(sc->numLev));
    for(i=0;i<=sc->numLev;i++)
        fscanf(fd,"%d",&(sc->levnBits[i]));

    return sc;
}

clientConf *
readClientConf(char *dirname)
{

    char filename[1000];
    char stashDIR[1000];
    FILE *fd;

    clientConf *cf=(clientConf *)malloc(sizeof(clientConf));



    sprintf(filename,"%s/SC.cnf",dirname);
    fd=fopen(filename,"r");
    cf->sc=readSC(fd);
    fclose(fd);
    cf->nBits     =(cf->sc->levnBits[MaxLev]);
    cf->nBlocks   =(1<<cf->nBits);
    cf->sStash    =(1<<(cf->sc->levnBits[0])); 
    cf->rBlocks   =cf->nBlocks-cf->sStash;
    cf->levSize=(int *)malloc((MaxLev+2)*sizeof(int));
    for(int j=0;j<=MaxLev;j++)
        cf->levSize[j]=(1<<(cf->sc->levnBits[j]));
    cf->levSize[MaxLev+1]=2*cf->levSize[MaxLev];
    
    sprintf(filename,"%s/Nops.cnf",dirname);
    fd=fopen(filename,"r");
    fscanf(fd,"%d",&(cf->numPhysOps));
    fscanf(fd,"%d",&(cf->numLogOps));
    fclose(fd);

    sprintf(filename,"%s/ND.cnf",dirname);
    fd=fopen(filename,"r");
    fscanf(fd,"%d",&(cf->nextDummy));
    fclose(fd);
    
    sprintf(filename,"%s/NS.cnf",dirname);
    fd=fopen(filename,"r");
    fscanf(fd,"%d",&(cf->nextStash));
    fclose(fd);
    
    sprintf(filename,"%s/levPM.cnf",dirname);
    fd=fopen(filename,"r");
    cf->levPM=readPM(fd);
    fclose(fd);
    
    sprintf(filename,"%s/posPM.cnf",dirname);
    fd=fopen(filename,"r");
    cf->posPM=readPM(fd);
    fclose(fd);
    
    sprintf(stashDIR,"%s/STASH",dirname);
    cf->stash=readStash(cf,stashDIR);
    
    return cf;
}
