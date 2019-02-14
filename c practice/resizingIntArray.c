#include <stdio.h>
#include <stdlib.h>
#include "resizingIntArray.h"

void init(ResizingArray *col) {
	col->size = 0;
	col->totalSize = 10;
	col->arr = malloc(sizeof(int)*col->totalSize);
}

void add(ResizingArray *col, int value) {
	if (col->size >= col->totalSize) {
		resize(ResizingArray *col);
	}
	col->arr[col->size] = value;
	col->size++;
}

int get (ResizingArray *col, int index) {
	return col->arr[index];
}

void set(ResizingArray *col, int value, int index) {
	while(index > col->totalSize) {
		resize(col);
	}
	col->arr[index] = value;
}

static void resize(ResizingArray *col) {
	int *new = malloc(sizeof(int)*(2*col->totalSize));
	for (int i = 0; i < col->totalSize; i++) {
		new[i] = col->arr[i];
	}
	col->arr = new;
	col->totalSize = (2*col->totalSize);
}

static void ResizingArrayFree(ResizingArray *col) {
	free(col->arr);
}