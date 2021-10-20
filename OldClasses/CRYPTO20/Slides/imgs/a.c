#include <unistd.h>


int
main()
{

char b[11];


/* password*/
b[0]='1';
b[1]='2';
b[2]='3';
/* salt */
b[3]=0x82;
b[4]=0x47;
b[5]=0xa8;
b[6]=0x16;
b[7]=0x8a;
b[8]=0xa8;
b[9]=0x52;
b[10]=0xfa;

/* send it to the stdout*/
write(1,b,11);

}
