#ICFSC        initClientfromSC
#WPPB         writePhysPlainBlock
#INITSTASH    initStash
#MERGESTASH   merge

DEBUG = -DICFSC 
DEBUG = -DMERGESTASH
CFLAGS = -g -Wno-incompatible-pointer-types -Wno-implicit-function-declaration ${DEBUG}

EXE=server setup read shuffle

all: ${EXE}
	
server: server.o xdr_filters.o
	gcc  $^ -o $@

shuffle: shuffle.o merge.o initC.o conf.o hlr.o llr.o xdr_filters.o 
	gcc  $^ -o $@

setup: setup.o initC.o conf.o hlr.o llr.o xdr_filters.o 
	gcc  $^ -o $@

read: read.o conf.o hlr.o llr.o xdr_filters.o 
	gcc  $^ -o $@

client: initC.o merge.o conf.o client.o hlr.o llr.o xdr_filters.o 
	gcc  $^ -o $@

clean:
	rm -f *o ${EXE}

