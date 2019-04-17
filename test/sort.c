#include <time.h>
#include <stdio.h>
#include <stdlib.h>
#include "my_qsort.h"

void print_table(int *A, int size) {
    printf("%%%%%%%%%%%%%%%%%%%%%%\n");
    for (int i = 0; i < size; ++i)
        printf("%d\n", A[i]);
    printf("%%%%%%%%%%%%%%%%%%%%%%\n");
}

int int_compare(const void *x, const void *y) {
    return *(int*) x - *(int*) y;
}

int main() {
    srand(time(NULL));
    int A[10];
    for (int i = 0; i < 10; ++i)
        A[i] = rand() % 100 + 1;

//    print_table(A, 10);
//    qsort((void*) A, 10, sizeof(int), int_compare);
//    print_table(A, 10);

    print_table(A, 10);
    my_qsort((void*) A, 10, sizeof(int), int_compare);
    print_table(A, 10);

    return 0;
}

