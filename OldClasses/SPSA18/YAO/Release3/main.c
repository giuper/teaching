#include <stdio.h>
#include "ds.h"
#include "templates.h"

int
main()
{

/*
    Gate circuit[]={{0,0,0,0,{0,0},3,"AND", andGate},
                {1,0,1,1,{0,0},3,"AND", andGate},
                {2,0,2,2,{0,0},4,"OR",  orGate},
                {3,1,1,1,{0,1},4,"OR",  orGate},
                {4,2,1,1,{2,3},8,"AND", andGate},
                };
*/

Gate circuit1[]={
                    {0,0,0,0,{0,0},{2,0},"OR",  orGate,{7,7},
                    {{(unsigned char *)NULL,(unsigned char *)NULL},
                     {(unsigned char *)NULL,(unsigned char *)NULL}},
                    {(unsigned  char *)NULL,(unsigned  char *)NULL}},
                    {1,0,1,1,{0,0},{2,1},"NAND", nandGate,{7,7},
                    {{(unsigned char *)NULL,(unsigned char *)NULL},
                     {(unsigned char *)NULL,(unsigned char *)NULL}},
                     {(unsigned  char *)NULL,(unsigned  char *)NULL}},
                    {2,2,1,1,{0,1},{8,8}, "XOR",xorGate,{7,7},
                    {{(unsigned char *)NULL,(unsigned char *)NULL},
                     {(unsigned char *)NULL,(unsigned char *)NULL}},
                     {(unsigned  char *)NULL,(unsigned  char *)NULL}},
                };
int a,b;

int x[]={0,0,1};
int y[]={0,0,1};

printFunct(circuit1,2);
printf("\n");

FILE *fd;
char fileName[80];
Gate *cir;
int l;

for (a=0;a<4;a++){
    for(b=0;b<4;b++){
        x[0]=a%2; y[0]=b%2;
        x[1]=(a>1)?1:0;
        y[1]=(b>1)?1:0;

        
        printf("The value of the function with");
        printf("\tX=[%d,%d]",x[0],x[1]);
        printf("\tY=[%d,%d]\t",y[0],y[1]);
        printf("is %d\t",evalFunct(circuit1,x,y,2));

        encode(circuit1,x,2);
        printf("encoded value is %d\t",decodeS(circuit1,y));
        sprintf(fileName,"Circuits/garCirc-%d%d-%d%d.txt",x[0],x[1],y[0],y[1]);
        fd=fopen(fileName,"w");
        fSelect(circuit1,y,3,fd);
        fclose(fd);
        
        fd=fopen(fileName,"r");
        cir=loadCircuit(fd,&l,y);
        fclose(fd);
        printf("and %d\n",decodeS(cir,y));
        
    }
}

}

