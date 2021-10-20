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

Gate circuit1[]={{0,0,0,0,{0,0},{2,0},"OR", orGate,{7,7},{{9,9},{9,9}},{8,8}},
                 {1,0,1,1,{0,0},{2,1},"AND", andGate,{7,7},{{9,9},{9,9}},{8,8}},
                 {2,2,1,1,{0,1},{8,8}, "XOR",  xorGate,{7,7},{{9,9},{9,9}},{8,8}},
                };
int a,b;

int x[]={0,1,1};
int y[]={1,1,1};

printFunct(circuit1,2);
printf("\n\n");

for (a=0;a<4;a++){
    for(b=0;b<4;b++){
        x[0]=a%2; y[0]=b%2;
        x[1]=(a>1)?1:0;
        y[1]=(b>1)?1:0;


    printf("\n\n");
    printf("The value of the function with\n");
    printf("\tX= %d %d\n",x[0],x[1]);
    printf("\tY= %d %d\n",y[0],y[1]);
    printf("is %d\n",evalFunct(circuit1,x,y,2));

    encode(circuit1,x,2);
    printf("The value of the encoded function\n");
    printf("is %d\n",decodeS(circuit1,y));
}
}

}

