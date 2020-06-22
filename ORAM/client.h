#include "go.h"

typedef struct clientConf {
    int numPhysOps;
    int numLogOps;
    int N;    /* total number of real blocks */
    int D;    /* total number of dummy blocks */
    int maxL; /* levels on server are 1,...,maxL-1 */
	serverConf *sc;
    int *n;   /* max number of real blocks by level */
    int *r;   /* number of blocks by level */
    int *f;   /* number of fillers by level */
    int *d;   /* number of dummies by level */
    int *s;   /* physical size of levels */
    int *ND;  /* next available dummy for each level */

    int *levPM;
    int *posPM;
    

    physPlainBlock **stash;
//    int NStash;

    
} clientConf;

/* physical level I/O */
void physWrite(physPlainBlock *,int,int);
physPlainBlock * physRead(int,int);
//void sequentialPhysScan(int);
//void moveToWorkTape();
//void moveFromWorkTape();
//void reShuffle();

/* logical level I/O */
//void logWrite(char block[], int);
physPlainBlock * logRead(int);

/* init operations */
void initClientfromSC(serverConf *sc);
void initStash();
clientConf *readClientConf(char *);
void writeClientConf(clientConf *, char *);
