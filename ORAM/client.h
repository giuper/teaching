#include "go.h"

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
void initStash();
void initServer();

