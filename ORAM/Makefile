#ICFSC        initClientfromSC
#WPPB         writePhysPlainBlock
#INITSTASH    initStash

DEBUG = -DICFSC -DWPPB
DEBUG = 
CFLAGS = -g -Wno-incompatible-pointer-types -Wno-implicit-function-declaration ${DEBUG}

EXE=server client read

all: ${EXE}
	
server: server.o xdr_filters.o
	gcc  $^ -o $@

read: read.o conf.o hlr.o llr.o xdr_filters.o 
	gcc  $^ -o $@

client: initC.o conf.o client.o hlr.o llr.o xdr_filters.o 
	gcc  $^ -o $@

clean:
	rm -f *o ${EXE}

