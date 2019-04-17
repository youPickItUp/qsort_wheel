CC=gcc
CWARN=-Wall -Werror
LIB_DIR=my_qsort/
TEST_DIR=test/
WRAPPER_DIR=my_qsort
define PYTHON_TEST
import $(WRAPPER_DIR).__init__ as wrapper
arr = [1, 3, 2]
wrapper.my_sort(arr, lambda x, y: x - y)
if arr == [1, 2, 3]:
	print("Success!")
else:
	print("Failure!")
endef


libmy_qsort.so: my_qsort.o
	$(CC) -shared -o $(LIB_DIR)$@ $^

my_qsort.o: my_qsort.c
	$(CC) -fPIC -c -o $@ $^ $(CWARN)

wheel: libmy_qsort.so
	python setup.py bdist_wheel
	pip install dist/*

.PHONY: clean

clean:
	rm -rf my_qsort.o $(LIB_DIR)libmy_qsort.so $(TEST_DIR)test dist build my_qsort.egg-info

test: libmy_qsort.so sort
	LD_LIBRARY_PATH=$(LIB_DIR) ./$(TEST_DIR)$@ && echo "SUCCESS!" || echo "FAILED!"

sort: $(TEST_DIR)sort.c
	$(CC) $^ -o $(TEST_DIR)test $(CWARN) -I. -lmy_qsort -L$(LIB_DIR) && echo "SUCCESS!" || echo "FAILED!"

export PYTHON_TEST
test_wrapper: libmy_qsort.so
	python -c "$$PYTHON_TEST"


