#include <stdio.h>
#include <rpc/rpc.h>
#include <string.h>

#include "go.h"


static physPlainBlock *memory[MaxNumLev+1];
//static int levSize[MaxNumLev+1];
static serverSetup sInfo;


#ifdef AAABBB

void
moveToWorkTape(int *pl)
{

    int lev=*pl;
    fprintf(stdout,"Move level %d to worktape\n",lev);
    for(int j=0;j<levSize[lev];j++)
        copyBlock(memory[MaxLev+1]+j,memory[lev]+j);
        
}

void
moveFromWorkTape(int *pl)
{

    int lev=*pl;
    fprintf(stdout,"Move worktape to level %d\n",lev);
    for(int j=0;j<levSize[lev];j++)
        copyBlock(memory[lev]+j,memory[MaxLev+1]+j);
        
}

#endif 

void
copyBlock(physPlainBlock *d, physPlainBlock *s)
{

    d->lev=s->lev;
    d->logInd=s->logInd;
    d->state=s->state;
    d->pos=s->pos;
    memcpy(d->block,s->block,sBlock);
}


physPlainBlock *
readPhysPlainBlock(rRequest *rr)
{


    physPlainBlock *res=(physPlainBlock *)malloc(sizeof(physPlainBlock));


    int lev=rr->lev;
    int pi=rr->physInd;
    if (pi>=sInfo.s[lev]){
   	    fprintf(stdout,"physical block %4d at lev %d (%d)\n",pi,lev,sInfo.s[lev]);
        fflush(stdout);
        return (physPlainBlock *)0;
    }
    physPlainBlock *Level=memory[lev];
    physPlainBlock *pPB=Level+pi;

   	//fprintf(stdout,"\treturning block with logId %d\n",pPB->logInd);

    return pPB;
}


int *
writePhysPlainBlock(wRequest *wr)
{


    int lev=wr->lev;
    int pos=wr->physInd;
    int *res=malloc(sizeof(int));
    *res=-25;

#ifdef WPPB
   	fprintf(stdout,"writing physical block: %d (log: %d) for lev %d %c\n",
                                pos,wr->pb->logInd,lev,wr->pb->block[0]);
#endif

    physPlainBlock *Level=memory[lev];
    physPlainBlock *pPB=Level+pos;
    
    
    if (pos<sInfo.s[lev]){ copyBlock(pPB,wr->pb); *res=1;}
    return res;
        
}
 
void *
buildLev(serverSetup *ss)
{

    fprintf(stdout,"here...\n");
    sInfo.maxL=ss->maxL;
    int maxL=sInfo.maxL;

    memory[0]=(physPlainBlock **) 0; /* lev 0 is on the client */
    for(int lev=1;lev<maxL;lev++){
        sInfo.s[lev]=ss->s[lev];
        memory[lev]=(physPlainBlock *)malloc(sInfo.s[lev]*sizeof(physPlainBlock));
    }
    sInfo.s[maxL]=sInfo.s[maxL-1];
    memory[maxL]=(physPlainBlock *)malloc(sInfo.s[maxL-1]*sizeof(physPlainBlock));
    fprintf(stdout,"Finishing...\n");
}



int
main(int argc, char **argv) 
{
	
	int res;

    
    fprintf(stdout,"running\n");

/*
    res=registerrpc(ORAMPROG,ORAMVERS,INIT_NUM,
        initServer, xdr_serverConf, xdr_void);

	res=registerrpc(ORAMPROG,ORAMVERS,MOVE_NUM,
        moveToWorkTape,xdr_int,xdr_void);

	res=registerrpc(ORAMPROG,ORAMVERS,BACK_NUM,
        moveFromWorkTape,xdr_int,xdr_void);
*/

	res=registerrpc(ORAMPROG,ORAMVERS,BUILDLEV_NUM,
        buildLev,xdr_serverSetup,xdr_void);

	res=registerrpc(ORAMPROG,ORAMVERS,WRITE_NUM,
        writePhysPlainBlock, xdr_wRequest, xdr_int);

	res=registerrpc(ORAMPROG,ORAMVERS,READ_NUM,
        readPhysPlainBlock, xdr_rRequest, xdr_physPlainBlock);
		
	svc_run();
	fprintf(stderr,"Errorr svc_run returned\n");
	exit(1);
}

