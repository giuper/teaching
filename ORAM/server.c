#include <stdio.h>
#include <rpc/rpc.h>
#include <string.h>

#include "go.h"


static physPlainBlock *memory[MaxNumLev];
static int levSize[MaxNumLev+1];
static int nOPs=0;


void resetTelemetry(){printf("Telemetry reset\n");nOPs=0;}
char *readTelemetry(){return (char *)&nOPs;}

char *
readPhysPlainBlock(Request *req)
{

    physPlainBlock *res=(physPlainBlock *)malloc(sizeof(physPlainBlock));

    int lev=req->lev;
    int pi=req->physInd;
    physPlainBlock *Level=memory[lev];
    physPlainBlock *pPB=Level+pi;

   	fprintf(stdout,"reading physical block: %2d at lev %d\n",req->physInd,req->lev);

    nOPs++;

    res->physInd=pi;
    res->logInd=pPB->logInd;
    memcpy(res->block,pPB->block,sBlock);
   	fprintf(stdout,"returning physical block: %2d at lev %d with logId %d\n",req->physInd,req->lev,res->logInd);

    return (char *)res;
}

void 
writePhysPlainBlock(Request *req)
{

   	fprintf(stdout,"writing physical block: %d (log: %d) for lev %d %c\n",
                                req->physInd,req->logInd,req->lev,req->block[0]);

    nOPs++;

    int lev=req->lev;
    int pi=req->physInd;
    physPlainBlock *Level=memory[lev];
    physPlainBlock *pPB=Level+pi;

    
    if (pi<levSize[lev]){
        memcpy(pPB->block,req->block,sBlock);
        pPB->logInd=req->logInd;
        pPB->physInd=req->physInd;
        pPB->block[1]='f'; pPB->block[2]='u';
        pPB->block[3]='c'; pPB->block[4]='k';
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
            ptr->physInd=j;
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
    for(j=0;j<levSize[sc->numLev+1];j++) memory[sc->numLev+1][j].dummy=1;

}

void
fakeInit()
{

    memory[0]=(physPlainBlock **) 0; /* lev 0 is on the client */
    memory[1]=(physPlainBlock *)malloc(8*sizeof(physPlainBlock));
    levSize[1]=8;

}

void
copyBlock(physPlainBlock *d, physPlainBlock *s)
{

    d->lev=s->lev;
    d->physInd=s->physInd; //this is irrelevant
    d->logInd=s->logInd;
    d->dummy=s->dummy;
    memcpy(d->block,s->block,sBlock);
}
    
void
moveToWorkTape(int *pl)
{

int lev=*pl;
fprintf(stdout,"Move level %d to worktape\n",lev);
for(int j=0; j<levSize[lev]; j++)
    copyBlock(memory[MaxLev+1]+j,memory[lev]+j);
        
}


int
main(int argc, char **argv) 
{
	
	int res;

    

    res=registerrpc(ORAMPROG,ORAMVERS,INIT_NUM,
        initServer, xdr_serverConf, xdr_void);

	res=registerrpc(ORAMPROG,ORAMVERS,READ_NUM,
        readPhysPlainBlock, xdr_Request, xdr_physPlainBlock);
		
	res=registerrpc(ORAMPROG,ORAMVERS,WRITE_NUM,
        writePhysPlainBlock, xdr_Request, xdr_void);

	res=registerrpc(ORAMPROG,ORAMVERS,RESET_TELEMETRY_NUM,
        resetTelemetry,xdr_void,xdr_void);
		
	res=registerrpc(ORAMPROG,ORAMVERS,READ_TELEMETRY_NUM,
        readTelemetry,xdr_void,xdr_int);
		
	res=registerrpc(ORAMPROG,ORAMVERS,MOVE_NUM,
        moveToWorkTape,xdr_int,xdr_void);
		

	svc_run();
	fprintf(stderr,"Errorr svc_run returned\n");
	exit(1);
}

