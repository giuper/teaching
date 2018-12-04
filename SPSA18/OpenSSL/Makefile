CFLAGS = -g
LDFLAGS = -L /usr/local/lib -lcrypto
obj=ex01RSA.o ex01DSA.o ex02.o ex02RSA.o ex02DSA.o ex03RSA.o ex04Enc.o ex05Dec.o ex06Sig.o ex07Ver.o 
targets=$(obj:.o=)

main: ${targets}

ex01RSA: ex01RSA.o
	gcc -o $@ $^ ${LDFLAGS}

ex01DSA: ex01DSA.o
	gcc -o $@ $^ ${LDFLAGS}

ex02: ex02.o
	gcc -o ex02 ex02.o ${LDFLAGS}

ex02RSA: ex02RSA.o
	gcc -o $@ $^ ${LDFLAGS}

ex02DSA: ex02DSA.o
	gcc -o $@ $^ ${LDFLAGS}

ex03RSA: ex03RSA.o
	gcc -o $@ $^ ${LDFLAGS}

ex04Enc: ex04Enc.o
	gcc -o $@ $^ ${LDFLAGS}

ex05Dec: ex05Dec.o
	gcc -o $@ $^ ${LDFLAGS}

ex06Sig: ex06Sig.o
	gcc -o $@ $^ ${LDFLAGS}

ex07Ver: ex07Ver.o
	gcc -o $@ $^ ${LDFLAGS}

clean:
	rm -f ${targets} ${obj}
	rm  KEYS/*
	rm  CT-SIG/*
