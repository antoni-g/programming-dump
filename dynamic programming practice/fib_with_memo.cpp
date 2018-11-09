// Example program
#include <iostream>
#include <string>
#include <vector>

int NIL = -1;
std::vector<int> memo(1000);

void init() {
    for (int i = 0; i < memo.size(); i++) {
        memo[i] = NIL;
    }
}

int fib(int n) {
    init();
    
    if (n == 0 || n == 1) {
        return 1;
    }    
    if (memo[n] != NIL) {
        return memo[n];
    }
    else {
        int res = fib(n-1) + fib(n-2);
        memo[n] = res;
        return res;
    }
}

int main()
{
    std::cout << fib(7);
}

