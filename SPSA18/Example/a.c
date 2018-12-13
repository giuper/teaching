#include <unistd.h>
#include <fcntl.h>



int
main(int argc, char *argv[])
{


char buf[2048];

int rd=open(argv[1],O_RDONLY);
int wd=open(argv[2],O_WRONLY|O_CREAT);
int br;

while ((br=read(rd,buf,2048))) write(wd,buf,br);
    


}
