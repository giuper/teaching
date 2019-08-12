CFLAGS = -g -DLOWLEVELDEBUG -Wno-incompatible-pointer-types -Wno-implicit-function-declaration
CFLAGS = -g -Wno-incompatible-pointer-types -Wno-implicit-function-declaration

EXE=server client setup read

read:   hlr.o sort.o llr.o initS.o xdr_filters.o read.o conf.o initC.o 
	gcc hlr.o sort.o llr.o initS.o xdr_filters.o read.o conf.o initC.o -o read

setup:  hlr.o sort.o llr.o initS.o xdr_filters.o setup.o conf.o initC.o 
	gcc hlr.o sort.o llr.o initS.o xdr_filters.o setup.o conf.o initC.o -o setup

server: server.o xdr_filters.o
	gcc xdr_filters.o server.o -o server

client: initC.o initS.o client.o xdr_filters.o llr.o hlr.o sort.o
	gcc initS.o initC.o client.o xdr_filters.o llr.o hlr.o sort.o -o client

clean:
	rm -f *o ${EXE}

all: ${EXE}
	
