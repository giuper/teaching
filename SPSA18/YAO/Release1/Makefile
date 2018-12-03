CFLAGS = 
CFLAGS = -g
LDFLAGS = -L/usr/lib/i386-linux-gnu/ -lssl -lcrypto 
OBJ=funcManagement.o main.o gateFunct.o encode.o decode.o

aes: aes.o
	gcc -o aes aes.o -L/usr/lib/i386-linux-gnu/ -lssl -lcrypto  

main: ${OBJ}
	gcc -o main ${OBJ}

clean: 
	rm -f main ${OBJ}
	rm -f aes aes.o

