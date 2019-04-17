CC=gcc
CWARN=-Wall -Werror
LIB_DIR=my_qsort/
TEST_DIR=test/

libmy_qsort.so: my_qsort.o
	$(CC) -shared -o $(LIB_DIR)$@ $^

my_qsort.o: my_qsort.c
	$(CC) -fPIC -c -o $@ $^ $(CWARN)

.PHONY: clean

clean:
	rm -f my_qsort.o $(LIB_DIR)libmy_qsort.so

test: libmy_qsort.so sort
	LD_LIBRARY_PATH=$(LIB_DIR) ./$(TEST_DIR)$@ && echo "SUCCESS!" || echo "FAILED!"

sort: $(TEST_DIR)sort.c
	$(CC) $^ -o $(TEST_DIR)test $(CWARN) -I. -lmy_qsort -L$(LIB_DIR) && echo "SUCCESS!" || echo "FAILED!"

