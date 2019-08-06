#include <stdio.h>
#include <rpc/rpc.h>
#include <string.h>

#include "go.h"


static physPlainBlock *memory[MaxNumLev];
static int levSize[MaxNumLev+1];


void
copyBlock(physPlainBlock *d, physPlainBlock *s)
{

    d->lev=s->lev;
    d->logInd=s->logInd;
    d->dummy=s->dummy;
    memcpy(d->block,s->block,sBlock);
}

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

physPlainBlock *
readPhysPlainBlock(rRequest *rr)
{

    physPlainBlock *res=(physPlainBlock *)malloc(sizeof(physPlainBlock));

    int lev=rr->lev;
    int pi=rr->physInd;
   	fprintf(stdout,"reading physical block: %2d at lev %d\n",rr->physInd,rr->lev);
    physPlainBlock *Level=memory[lev];
    physPlainBlock *pPB=Level+pi;

   	fprintf(stdout,"\treturning block with logId %d\n",pPB->logInd);

    return (char *)pPB;
}

void 
writePhysPlainBlock(wRequest *wr)
{

    int lev=wr->lev;
    int pi=wr->physInd;
   	fprintf(stdout,"writing physical block: %d (log: %d) for lev %d %c\n",
                                pi,wr->pb->logInd,lev,wr->pb->block[0]);

    physPlainBlock *Level=memory[lev];
    physPlainBlock *pPB=Level+pi;

    
    if (pi<levSize[lev]){
        copyBlock(pPB,wr->pb);
    }
}
 
void
initServer(serverConf *sc)
{

    physPlainBlock *ptr;
    int j,lev;

    memory[0]=(physPlainBlock **) 0; /* lev 0 is on the client */

/* levels 1...numLev-1 are initialized to contain dummy blocks */
/* tbr */
    for(lev=1;lev<sc->numLev;lev++){
        levSize[lev]=(1<<(sc->levnBits[lev]));
        memory[lev]=(physPlainBlock *)malloc(levSize[lev]*sizeof(physPlainBlock));
        for(j=0,ptr=memory[lev];j<levSize[lev];j++,ptr++){
            ptr->lev=lev;
            ptr->logInd=j;
            ptr->dummy=1;  /* dummy */
        }
    }
    /* the last active lev is initialized by the client  
       so we only allocate memory */
    levSize[sc->numLev]=(1<<(sc->levnBits[sc->numLev]));
    memory[sc->numLev]=(physPlainBlock *)malloc(levSize[sc->numLev]*sizeof(physPlainBlock));

    /* we initialize the work tape */
    levSize[sc->numLev+1]=2*levSize[sc->numLev];
    memory[sc->numLev+1]=(physPlainBlock *)malloc(levSize[sc->numLev+1]*sizeof(physPlainBlock));
    for(j=0;j<levSize[sc->numLev+1];j++){
        memory[sc->numLev+1][j].dummy=1;
        memory[sc->numLev+1][j].logInd=levSize[sc->numLev+1];
        memory[sc->numLev+1][j].block[0]='%';
        memory[sc->numLev+1][j].block[1]='%';
    }

}


int
main(int argc, char **argv) 
{
	
	int res;

    

    res=registerrpc(ORAMPROG,ORAMVERS,INIT_NUM,
        initServer, xdr_serverConf, xdr_void);

	res=registerrpc(ORAMPROG,ORAMVERS,READ_NUM,
        readPhysPlainBlock, xdr_rRequest, xdr_physPlainBlock);
		
	res=registerrpc(ORAMPROG,ORAMVERS,WRITE_NUM,
        writePhysPlainBlock, xdr_wRequest, xdr_void);

	res=registerrpc(ORAMPROG,ORAMVERS,MOVE_NUM,
        moveToWorkTape,xdr_int,xdr_void);

	res=registerrpc(ORAMPROG,ORAMVERS,BACK_NUM,
        moveFromWorkTape,xdr_int,xdr_void);
/*
	res=registerrpc(ORAMPROG,ORAMVERS,RESET_TELEMETRY_NUM,
        resetTelemetry,xdr_void,xdr_void);
		
	res=registerrpc(ORAMPROG,ORAMVERS,READ_TELEMETRY_NUM,
        readTelemetry,xdr_void,xdr_int);
		
*/
		

	svc_run();
	fprintf(stderr,"Errorr svc_run returned\n");
	exit(1);
}

