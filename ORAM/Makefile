CFLAGS = -g -DLOWLEVELDEBUG -Wno-incompatible-pointer-types -Wno-implicit-function-declaration
CFLAGS = -g -Wno-incompatible-pointer-types -Wno-implicit-function-declaration

all: server client
	

server: server.o xdr_filters.o
	gcc xdr_filters.o server.o -o server

client: init.o client.o xdr_filters.o llr.o hlr.o sort.o
	gcc init.o client.o xdr_filters.o llr.o hlr.o sort.o -o client

clean:
	rm -f *o server client
