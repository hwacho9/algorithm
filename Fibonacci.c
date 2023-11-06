#include <stdio.h>

int fib(int n)
{
    int f, f1, f2;

    f2 = 0; f1 = 1;
    for (int i= 2; i<=n; i++) {
        f = f2 + f1;
        f2 = f1; f1 = f;     
    }

    return f;
}

int main (void)
{
    int n = 10;
    int result;

    result = fib(n);

    printf("%d", result);
    return 0;
}