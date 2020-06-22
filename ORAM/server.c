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
    if (pi>sInfo.s[lev]){
        int x=0;
    }
   	//fprintf(stdout,"reading physical block: %2d at lev %d\n",rr->physInd,rr->lev);
    physPlainBlock *Level=memory[lev];
    physPlainBlock *pPB=Level+pi;

   	//fprintf(stdout,"\treturning block with logId %d\n",pPB->logInd);

    return (char *)pPB;
}


void 
writePhysPlainBlock(wRequest *wr)
{


    int lev=wr->lev;
    int pos=wr->physInd;
#ifdef WPPB
   	fprintf(stdout,"writing physical block: %d (log: %d) for lev %d %c\n",
                                pos,wr->pb->logInd,lev,wr->pb->block[0]);
#endif

    physPlainBlock *Level=memory[lev];
    physPlainBlock *pPB=Level+pos;
    
    if (pos<sInfo.s[lev]) copyBlock(pPB,wr->pb);
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
        writePhysPlainBlock, xdr_wRequest, xdr_void);

	res=registerrpc(ORAMPROG,ORAMVERS,READ_NUM,
        readPhysPlainBlock, xdr_rRequest, xdr_physPlainBlock);
		

	svc_run();
	fprintf(stderr,"Errorr svc_run returned\n");
	exit(1);
}

