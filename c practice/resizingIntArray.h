typedef struct {
	int size;
	int totalSize;
	int *arr;
} ResizingArray;

void init(ResizingArray *col);
void add(ResizingArray *col, int value);
int get(ResizingArray *col, int index);
static void resize(ResizingArray *col);
void set(ResizingArray *col, int value, int index);
static void ResizingArrayFree(ResizingArray *col);