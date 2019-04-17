CC=gcc
LIB_DIR=my_qsort/

libmy_qsort.so: my_qsort.o
	$(CC) -shared -o $(LIB_DIR)$@ $^

my_qsort.o: my_qsort.c
	$(CC) -fPIC -c -o $@ $^ -Wall -Werror

clean:
	rm -f my_qsort.o $(LIB_DIR)libmy_qsort.so

