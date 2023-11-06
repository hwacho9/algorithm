#include <stdio.h>

int fil(int n)
{
    if ( n == 0 || n == 1)
        return n;

    return fib(n-2) + fib(n-1);
}

int main(void)
{
    int n =10;
    int result;

    result = fib(n);

    return 0;
}