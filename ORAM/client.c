#include <stdio.h>
#include <stdlib.h>
#include <rpc/rpc.h>
#include "client.h"

serverConf sc={1,{5,10,0,0,0,0,0,0,0,0}};

int nBits, nBlocks, sStash, rBlocks;
int nextStash, nextDummy;


int rwapCNT;
physPlainBlock **stash;

int *levPM, *posPM;
int levSize[MaxNumLev+1];

int numPhysOps=0;
int numLogOps=0;


int
main(int argc, char **argv)
{

    physPlainBlock *res;
    int nSOPs=0;
    int i,j,k;
    int stat;

    nBits     =(sc.levnBits[MaxLev]);
    nBlocks   =(1<<nBits);
    sStash    =(1<<(sc.levnBits[0])); 
    rBlocks   =nBlocks-sStash;
    nextDummy =nBlocks-sStash; /*logical identifier of next unread dummy block*/

    levPM=(int *)malloc(nBlocks*sizeof(int));
    posPM=(int *)malloc(nBlocks*sizeof(int));

    fprintf(stdout,"client: starting...\n");
    fprintf(stdout,"\tnBlocks   =%5d\n",nBlocks);
    fprintf(stdout,"\tsStash    =%5d\n",sStash);
    fprintf(stdout,"\tnextDummy =%5d\n",nextDummy);
    fprintf(stdout,"\trBlocks   =%5d\n",nBlocks-sStash);
    fprintf(stdout,"client: init...");
    initStash();
    initServer();
    fprintf(stdout,"completed\n");

    stat=callrpc("localhost", ORAMPROG, ORAMVERS, 
        RESET_TELEMETRY_NUM,
		xdr_void, (void *)0,
		xdr_void, (void *)0);
    if (stat<0){
	    clnt_perrno(stat);
		exit(1);
    }


    for (int k=0;k<16;k++){
        res=logRead(k);if(res){fprintf(stdout,"RR: %4d-->%s\n",k,res->block); }
        res=logRead(k);if(res){fprintf(stdout,"RR: %4d-->%s\n",k,res->block); }
    }
    

    stat=callrpc("localhost", ORAMPROG, ORAMVERS, 
        READ_TELEMETRY_NUM,
		xdr_void,(void *)0,
		xdr_int, &nSOPs); 
    if (stat<0){
	    clnt_perrno(stat);
		exit(1);
    }
    fprintf(stdout,"Total number of ops=%5d\n",nSOPs);


    for (int k=0;k<200;k++){
        res=logRead(k);if(res){fprintf(stdout,"RR: %4d-->%s\n",k,res->block);free(res); }
    }


/*
    stat=callrpc("localhost", ORAMPROG, ORAMVERS, 
        READ_TELEMETRY_NUM,
		xdr_void,(void *)0,
		xdr_int, &nSOPs); 
    if (stat<0){
	    clnt_perrno(stat);
		exit(1);
    }
    fprintf(stdout,"Total number of ops=%5d\n",nSOPs);
*/

    for (int i=0;i<4;i++){
        k=2;res=logRead(k);  if(res){fprintf(stdout,"RR: %4d-->%s\n",k,res->block);free(res);}
        k=22;res=logRead(k); if(res){fprintf(stdout,"RR: %4d-->%s\n",k,res->block);free(res);}
        k=32;res=logRead(k); if(res){fprintf(stdout,"RR: %4d-->%s\n",k,res->block);free(res);}
    }

    for (int k=0;k<nBlocks;k++){
        res=logRead(k);   if(res){fprintf(stdout,"RR: %4d-->%s\n",k,res->block);free(res);}
        res=logRead(k+1); if(res){fprintf(stdout,"RR: %4d-->%s\n",k+1,res->block);free(res);}
        res=logRead(k);   if(res){fprintf(stdout,"RR: %4d-->%s\n",k,res->block);free(res);}
    }


/*
    stat=callrpc("localhost", ORAMPROG, ORAMVERS, 
        READ_TELEMETRY_NUM,
		xdr_void,(void *)0,
		xdr_int, &nSOPs); 
    if (stat<0){
	    clnt_perrno(stat);
		exit(1);
    }
*/

    fprintf(stdout,"Total number of logical  ops=%6d\n",numLogOps);
    fprintf(stdout,"Total number of physical ops=%6d\n",numPhysOps);
    fprintf(stdout,"Slowdown                    =%6d\n",numPhysOps/numLogOps);

	exit(0);

}
