// Example program
#include <iostream>
#include <string>
#include <vector>

std::vector<int> memo(1000);

int fib(int n) {
    memo[0] = 1;
    memo[1] = 1;
    for (int i = 2; i <= n; i++) {
        memo[i] = memo[i - 1] + memo[i-2];
    }
    return memo[n];
}

int main()
{
    std::cout << fib(7);
}

