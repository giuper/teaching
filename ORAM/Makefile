CFLAGS = -DTELEMETRY -DBSORT -Wno-incompatible-pointer-types -Wno-implicit-function-declaration
CFLAGS = -g -DTELEMETRY -Wno-incompatible-pointer-types -Wno-implicit-function-declaration
CC=gcc

all: server client
	

server: server.o xdr_filters.o
	gcc xdr_filters.o server.o -o server

client: client.o xdr_filters.o sort.o
	gcc xdr_filters.o client.o sort.o -o client

clean:
	rm -f *o server client
