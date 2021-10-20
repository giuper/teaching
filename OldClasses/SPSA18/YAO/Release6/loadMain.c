#include <stdio.h>
#include "ds.h"
#include "templates.h"

int
main(int argc, char **argv)
{

    Gate *circuit;
    int y[]={0,0};
    int l;

    if (argc!=2){
        fprintf(stderr,"Missing argument\n");
        return 1;
    }
    FILE *fd=fopen(argv[1],"r");
    circuit=loadCircuit(fd,&l,y);

    fSelect(circuit,y,l,stdout);

    printf("Value is %d*\n",decodeS(circuit,y));

    return 0;
}
