#include <time.h>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include "my_qsort.h"

void swap(char *x, char *y, int size) {
    char tmp;
    for (int i = 0; i < size; ++i) {
        tmp = x[i];
        x[i] = y[i];
        y[i] = tmp;
    }
}

void my_qsort(void *A, int num, int size, int (*compare)(const void*, const void*)) {
    if (num <= 1)
        return;
    srand(time(NULL));
    int pivot_idx = rand() % num;
    char *pivot = (char*) A + pivot_idx * size;
    swap((char*) A, pivot, size);
    pivot = (char*) A;

    char *begin = (char*) A;
    char *end   = (char*) A + num * size;
    while (begin < end) {
        begin += size;
        while (compare((void*) begin, (void*) pivot) < 0 && begin < end)
            begin += size;
        end -= size;
        while (compare((void*) end, (void*) pivot) > 0 && begin < end)
            end -= size;
        if (begin < end)
            swap (begin, end, size);
    }
    if (compare((void*) end, (void*) pivot) > 0)
        end -= size;
    swap ((void*)end, (void*)pivot, size);
    int num1 = (int)(end - (char*) A) / size;

    my_qsort(A, num1, size, compare);
    my_qsort((void*) (end+size), num - num1 - 1, size, compare);
}

