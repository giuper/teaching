#define ORAMPROG ((u_long) 1300002)
#define ORAMVERS ((u_long) 1)

#define INIT_NUM            ((u_long) 9)
#define READ_TELEMETRY_NUM  ((u_long) 2)
#define RESET_TELEMETRY_NUM ((u_long) 3)
#define WRITE_NUM           ((u_long) 4)
#define READ_NUM            ((u_long) 5)
#define MOVE_NUM            ((u_long) 6)
#define BACK_NUM            ((u_long) 7)


#define sBlock     1024    /* in bytes */
#define MaxNumLev    10  
#define MaxLev        1    /* levels are 0,1,...,MaxLev */

typedef struct serverConf {
	int numLev;
	int levnBits[MaxNumLev];
} serverConf;


typedef struct physPlainBlock {
    int lev;
	int logInd;
    int dummy;
    int pos; //only used for reShuffling
	char block[sBlock];
} physPlainBlock;

typedef struct wRequest {
    int lev;
	int physInd;
    physPlainBlock *pb;
} wRequest;

typedef struct rRequest {
    int lev;
	int physInd;
} rRequest;

int xdr_serverConf    (XDR *, serverConf *);
int xdr_physPlainBlock(XDR *, physPlainBlock *);
int xdr_wRequest  (XDR *, wRequest *);
int xdr_rRequest  (XDR *, rRequest *);

