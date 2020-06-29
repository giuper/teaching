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

    fprintf(fd,"%d\n",sc->maxL);
    for(i=0;i<=MaxNumLev;i++) fprintf(fd,"%d\n",sc->nb[i]);
}

serverConf *
readSC(FILE *fd)
{
    int i;

    serverConf *sc=(serverConf *)malloc(sizeof(serverConf));

    fscanf(fd,"%d",&(sc->maxL));
    for(i=0;i<=MaxNumLev;i++) fscanf(fd,"%d",&(sc->nb[i]));

    return sc;
}

void
writeStash(clientConf *cf, char *dirname)
{

    int i,fd;
    FILE *ffd;
    char filename[100];

    for(i=0;i<cf->ND[0];i++){
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

physPlainBlock **
readStash(clientConf *cf, char *dirname)
{

    int i,fd;
    FILE *ffd;
    char filename[100];
    physPlainBlock **stash=(physPlainBlock **)malloc(cf->n[0]*sizeof(physPlainBlock));

    //printf("nextStash=%d\n",cf->nextStash);
    for(i=0;i<cf->ND[0];i++){
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
        stash[i]->state=REAL;
    }
    for(i=cf->ND[0];i<cf->n[0];i++)
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

void
writeClientConf(clientConf *cf, char *dirname)
{

    char filename[1000];
    char stashDIR[1000];
    FILE *fd;

    mkdir(dirname,0777);

    sprintf(filename,"%s/General.cnf",dirname);
    fd=fopen(filename,"w");
    fprintf(fd,"%d\n",cf->numPhysOps);
    fprintf(fd,"%d\n",cf->numLogOps);
    fprintf(fd,"%d\n",cf->N);
    fprintf(fd,"%d\n",cf->D);
    fprintf(fd,"%d\n",cf->maxL);
    fclose(fd);

    sprintf(filename,"%s/SC.cnf",dirname);
    fd=fopen(filename,"w");
    writeSC(fd,cf->sc);
    fclose(fd);

    sprintf(filename,"%s/n.cnf",dirname);
    fd=fopen(filename,"w");
    writePM(fd,cf->n,cf->maxL);
    fclose(fd);
    
    cf->r[0]=cf->ND[0];
    sprintf(filename,"%s/r.cnf",dirname);
    fd=fopen(filename,"w");
    writePM(fd,cf->r,cf->maxL);
    fclose(fd);
    
    sprintf(filename,"%s/f.cnf",dirname);
    fd=fopen(filename,"w");
    writePM(fd,cf->f,cf->maxL);
    fclose(fd);
    
    sprintf(filename,"%s/d.cnf",dirname);
    fd=fopen(filename,"w");
    writePM(fd,cf->d,cf->maxL);
    fclose(fd);
    
    sprintf(filename,"%s/s.cnf",dirname);
    fd=fopen(filename,"w");
    writePM(fd,cf->s,cf->maxL);
    fclose(fd);
    
    sprintf(filename,"%s/ND.cnf",dirname);
    fd=fopen(filename,"w");
    writePM(fd,cf->ND,cf->maxL);
    fclose(fd);
    
    sprintf(filename,"%s/levPM.cnf",dirname);
    fd=fopen(filename,"w");
    writePM(fd,cf->levPM,cf->N+cf->D);
    fclose(fd);
    
    sprintf(filename,"%s/posPM.cnf",dirname);
    fd=fopen(filename,"w");
    writePM(fd,cf->posPM,cf->N+cf->D);
    fclose(fd);
    
    sprintf(stashDIR,"%s/STASH",dirname);
    mkdir(stashDIR,0777);
    writeStash(cf,stashDIR);
}

clientConf *
readClientConf(char *dirname)
{

    char filename[1000];
    char stashDIR[1000];
    FILE *fd;

    clientConf *cf=(clientConf *)malloc(sizeof(clientConf));

    sprintf(filename,"%s/General.cnf",dirname);
    fd=fopen(filename,"r");
    fscanf(fd,"%d",&(cf->numPhysOps));
    fscanf(fd,"%d",&(cf->numLogOps));
    fscanf(fd,"%d",&(cf->N));
    fscanf(fd,"%d",&(cf->D));
    fscanf(fd,"%d",&(cf->maxL));
    fclose(fd);

    sprintf(filename,"%s/SC.cnf",dirname);
    fd=fopen(filename,"r");
    cf->sc=readSC(fd);
    fclose(fd);

    sprintf(filename,"%s/n.cnf",dirname);
    fd=fopen(filename,"r");
    cf->n=readPM(fd);
    fclose(fd);
    
    sprintf(filename,"%s/r.cnf",dirname);
    fd=fopen(filename,"r");
    cf->r=readPM(fd);
    fclose(fd);
    
    sprintf(filename,"%s/f.cnf",dirname);
    fd=fopen(filename,"r");
    cf->f=readPM(fd);
    fclose(fd);
    
    sprintf(filename,"%s/d.cnf",dirname);
    fd=fopen(filename,"r");
    cf->d=readPM(fd);
    fclose(fd);
    
    sprintf(filename,"%s/s.cnf",dirname);
    fd=fopen(filename,"r");
    cf->s=readPM(fd);
    fclose(fd);
    
    sprintf(filename,"%s/ND.cnf",dirname);
    fd=fopen(filename,"r");
    cf->ND=readPM(fd);
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
