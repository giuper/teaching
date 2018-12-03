#include <stdio.h>
#include "ds.h"
#include "templates.h"

int
main()
{

#include "circuit-7.h"

int a,b,i;
int x[NumINP], y[NumINP];
int max=1<<NumINP;
int cv, ncv;

printFunct(circuit,NumGates-1); printf("\n");

for (a=0;a<max;a++){
    for(b=0;b<max;b++){
        for(i=0;i<NumINP;i++){
            x[i]=(a&(1<<i))>>i;
            y[i]=(b&(1<<i))>>i;
        }
        printf("The value of the function with\tX=[");
        printf("%d",x[0]);
        for(i=1;i<NumINP;i++) printf(",%d",x[i]);
        printf("]\tY=[");
        printf("%d",y[0]);
        for(i=1;i<NumINP;i++) printf(",%d",y[i]);
        printf("]\t");
        ncv=evalFunct(circuit,x,y,NumGates-1);
        encode(circuit,x,NumGates-1);
        cv=decode(circuit,NumGates-1,y);
        printf("is %d",ncv);
        printf("\tencoded value is %d",(int) cv);
        if (ncv!=cv) printf(" *");
        printf("\n");
    }
}

}
