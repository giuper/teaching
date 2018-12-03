#include "ds.h"
void encodeOutput(Gate *,Gate *);
void encodeInput(Gate *,Gate *,int *);

void
encode(Gate *circuit,int *x,int l)
{

    int i;
    Gate *current;

    for(i=0;i<=l;i++){
        current=circuit+i;

        current->gb[0]=0;
        current->gb[1]=1;
        
        current->keys[0]=0;
        current->keys[1]=1;
    }

    for(i=0;i<=l;i++){
        current=circuit+i;
        if (current->type==2)
            encodeOutput(circuit,current);
        if (current->type==0)
            encodeInput(circuit,current,x);
    }
}

   

void
encodeOutput(Gate *circuit,Gate *current)
{

    int b0,b1;
    int r,c;
    int res;
    Gate *p0,*p1;

    b0=current->gb[0]; b1=current->gb[1];
    p0=circuit+current->pGate[0]; p1=circuit+current->pGate[1];
    for(r=0;r<2;r++){
        for(c=0;c<2;c++){
            res=current->funct(b0^r,b1^c);     
            current->table[r][c]=p0->keys[r^b0]^p1->keys[c^b1]^res;
        }
    }
}


void
encodeInput(Gate *circuit,Gate *current,int *x)
{

    int r, res;
    int xinp=x[current->xIndex];
    Gate *ng=circuit+current->nGate[0];
    int ngb=ng->gb[current->nGate[1]];

    for(r=0;r<2;r++){
        res=current->funct(xinp,r);
        current->table[r][0]=current->keys[res];
        current->table[r][1]=res^ngb;
    }
}
