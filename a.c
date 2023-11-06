#include <stdio.h>
#define n 5

void dec2bin(int i, int x[]);

int main(void) 
{
    int a[n] = {8, 12, 22, 15, 13};
    int b = 47;
    int x[n] = {0, 0, 0, 0, 0};
    int sum;
    int p = 0;

    for (int i = 0; i < 32; i++) {
        dec2bin(i, x);
        sum = 0; 
        for (int j = 0; j < n; j++) {
            sum += a[j] * x[j];
            p++;
        }
        if (sum == b) {
            printf("%d\nYES\n",p);
            return 0;
        }
    }
    printf("%d\n",p);
    printf("NO\n");
    return 0;
}

void dec2bin(int i, int x[]) {
    for (int j = 0; j < n; j++) {
        x[j] = (i >> j) & 1;
    }
}
