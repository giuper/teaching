#include <stdio.h>
#include <stdlib.h>
#include <rpc/rpc.h>
#include "client.h"

serverConf sc={1,{2,4,0,0,0,0,0,0,0,0}};

int nBits, nBlocks, sStash;
int nextStash, nextDummy;


int rwapCNT;
physPlainBlock **stash;

int *perm; 
int *levPM, *posPM;
int levSize[MaxNumLev+1];

int numOps, totalNumOps;


int
main(int argc, char **argv)
{

    physPlainBlock *res;
    int nSOPs;

    nBits     =(sc.levnBits[MaxLev]);
    nBlocks   =(1<<nBits);
    sStash    =(1<<(sc.levnBits[0])); 
    nextDummy=nBlocks/2; /*logical identifier of next unread dummy block*/
    nextDummy=nBlocks-sStash; /*logical identifier of next unread dummy block*/

    perm=(int *)malloc(nBlocks*sizeof(int));
    levPM=(int *)malloc(nBlocks*sizeof(int));
    posPM=(int *)malloc(nBlocks*sizeof(int));

    fprintf(stdout,"client: starting...\n");
    fprintf(stdout,"\tnBlocks   =%5d\n",nBlocks);
    fprintf(stdout,"\tsStash    =%5d\n",sStash);
    fprintf(stdout,"\tnextDummy =%5d\n",nextDummy);
    fprintf(stdout,"\tnRBlocks  =%5d\n",nBlocks-sStash);
    fprintf(stdout,"client: init...");
    initStash();
    initServer();
    fprintf(stdout,"completed\n");

    sequentialPhysScan(MaxLev);

    

    res=logRead(0);    
    fprintf(stdout,"0 --> %c%c\n",res->block[0],res->block[1]);
    res=logRead(1);    
    fprintf(stdout,"1 --> %c%c\n",res->block[0],res->block[1]);
    res=logRead(0);    
    fprintf(stdout,"0 --> %c%c\n",res->block[0],res->block[1]);
    res=logRead(0);    
    fprintf(stdout,"0 --> %c%c\n",res->block[0],res->block[1]);

    fprintf(stdout,"\n\nAAAA\n");
    sequentialPhysScan(MaxLev);
    fprintf(stdout,"AAAA\n\n");
    reShuffle();
    sequentialPhysScan(MaxLev);
    initStash();

    fprintf(stdout,"\n\nBBBB\n");
    res=logRead(0);    
    fprintf(stdout,"0 --> %c%c\n",res->block[0],res->block[1]);
    res=logRead(1);    
    fprintf(stdout,"1 --> %c%c\n",res->block[0],res->block[1]);
    res=logRead(0);    
    fprintf(stdout,"0 --> %c%c\n",res->block[0],res->block[1]);
    res=logRead(0);    
    fprintf(stdout,"0 --> %c%c\n",res->block[0],res->block[1]);

    fprintf(stdout,"\n\nAAAA\n");
    sequentialPhysScan(MaxLev);
    fprintf(stdout,"AAAA\n\n");
    reShuffle();
    sequentialPhysScan(MaxLev);
    initStash();

    fprintf(stdout,"\n\nBBBB\n");
    res=logRead(0);    
    fprintf(stdout,"0 --> %c%c\n",res->block[0],res->block[1]);
    res=logRead(3);    
    fprintf(stdout,"3 --> %c%c\n",res->block[0],res->block[1]);
    res=logRead(0);    
    fprintf(stdout,"0 --> %c%c\n",res->block[0],res->block[1]);
    res=logRead(8);    
    fprintf(stdout,"8 --> %c%c\n",res->block[0],res->block[1]);

    fprintf(stdout,"\n\nAAAA\n");
    sequentialPhysScan(MaxLev);
	exit(0);

}
