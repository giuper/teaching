#include <stdio.h>
#include "ds.h"
#include "templates.h"

int
main()
{

    #include "circuit-7.h"

    int a,b,i,ss;
    int x[NumINP], y[NumINP];
    int max=1<<NumINP;
    int cv,ev,rcv;
    int outputGateIndex=NumGates-1; //the output gate is the last gate
    char filename[100];
    FILE *fd;
    Gate *rCircuit;
    
    printFunct(circuit,outputGateIndex); printf("\n");

    for (a=0;a<max;a++){
        for(b=0;b<max;b++){
            for(i=0;i<NumINP;i++){
                x[i]=(a&(1<<i))>>i;
                y[i]=(b&(1<<i))>>i;
            }

            ev=evalFunct(circuit,x,y,outputGateIndex);
            printf("The value of the function with\tX=[");
            printf("%d",x[0]);
            for(i=1;i<NumINP;i++) printf(",%d",x[i]);
            printf("] Y=[");
            printf("%d",y[0]);
            for(i=1;i<NumINP;i++) printf(",%d",y[i]);
            printf("] is %d",ev);

            encode(circuit,x,NumGates);
            selectGarb(circuit,y,NumGates);
            //cv=decode(circuit,outputGateIndex);
            //printf("\tencoded value is %d",(int) cv);

            sprintf(filename,"Circuits/garbled-%d-%d.txt",a,b);
            fd=fopen(filename,"w"); 
            writeGarb(circuit,NumGates,fd);
            fclose(fd);

            fd=fopen(filename,"r"); 
            rCircuit=readGarb(fd,&ss);
            fclose(fd);

            rcv=decode(rCircuit,ss-1);
            printf(" encoded value is %d",rcv);
            if (rcv!=ev) printf(" *");
            printf("\n");
        }
    }
}
