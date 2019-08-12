#include "go.h"

typedef struct clientConf {
	serverConf *sc;
    int nBits;
    int nBlocks;
    int rBlocks;
    int nextDummy;
    int nextStash;
    int sStash;
    int *levPM;
    int *posPM;
    physPlainBlock **stash;
    int *levSize;
    int numPhysOps;
    int numLogOps;

} clientConf;

/* physical level I/O */
void physWrite(physPlainBlock *,int,int);
physPlainBlock * physRead(int,int);
void sequentialPhysScan(int);
void moveToWorkTape();
void moveFromWorkTape();
void reShuffle();

/* logical level I/O */
void logWrite(char block[], int);
physPlainBlock * logRead(int);

/* init operations */
void initClientfromSC(serverConf *sc);
void initStash();
clientConf *readClientConf(char *);
void writeClientConf(clientConf *, char *);
