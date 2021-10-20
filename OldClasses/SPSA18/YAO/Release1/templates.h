void printFunct(Gate *,int);
int evalFunct(Gate *,int *,int *,int);

void encode(Gate *,int *,int);
int decodeS(Gate *,int *);

extern int andGate(int,int);
extern int nandGate(int,int);
extern int orGate(int,int);
extern int norGate(int,int);
extern int xorGate(int,int);
extern int nxorGate(int,int);
