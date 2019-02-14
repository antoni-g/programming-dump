#include <iostream>
#include <vector>

using namespace std;

class MinHeap {
	public:
		MinHeap() {
			arr = vector<int>();
		}
		int peek(void);
		void insert(int i);

	protected:
		vector<int> arr;
		int getLeftChildIndex(int parent);
		int getRightChildIndex(int parent);
		int getParentIndex(int tgt);
		bool hasLeftChild(int parent);
		bool hasRightChild(int parent);
		bool hasParent(int tgt);
		int getLeftChild(int parent);
		int getRightChild(int parent);
		int getParent(int tgt);
};

int MinHeap::getLeftChildIndex(int parent) {
	return 2*parent + 1;
}

int MinHeap::getRightChildIndex(int parent) {
	return 2*parent + 2;
}

int MinHeap::getParentIndex(int tgt) {
	return (tgt-1)/2;
}

bool MinHeap::hasRightChild(int parent) {
	return getRightChildIndex(parent) < arr.size();
}

bool MinHeap::hasLeftChild(int parent) {
	return getLeftChildIndex(parent) < arr.size();
}

bool MinHeap::hasParent(int tgt) {
	return tgt > 0;
}

int MinHeap::getLeftChild(int parent) {
	return arr.at(getLeftChildIndex(parent));
}

int MinHeap::getRightChild(int parent) {
	return arr.at(getRightChildIndex(parent));
}

int MinHeap::getParent(int tgt) {
	return arr.at(getParentIndex(tgt));
}

int MinHeap::peek(void) {
	if (arr.size() <= 0) {
		throw std::length_error("called peek on an empty MinHeap");
	} else {
		return arr.front();
	}
}

void MinHeap::insert(int i) {
	arr.push_back(i);
	// bubble up if necessary
	if (arr.size() > 1) {

	}
}


int main ()
{

  MinHeap heap;
  heap.insert(2);
  cout << heap.peek();

  return 0;
}