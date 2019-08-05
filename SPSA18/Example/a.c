#include <unistd.h>
#include <fcntl.h>
#include <stdio.h>



int
main(int argc, char *argv[])
{


char buf[2048];

int rd=open(argv[1],O_RDONLY);
int wd=open(argv[2],O_WRONLY|O_CREAT);
int br;

printf("size of file %d\n",(int) lseek(rd,0,SEEK_END));
lseek(rd,0,SEEK_SET);
while ((br=read(rd,buf,2048))) write(wd,buf,br);
    


}
