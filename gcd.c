#include<stdio.h>
int main(void)
{
    int a = 2528, b =395;
    int x,y,z;
    int gcd;

    x = a;
    y = b;

    int num = 0;

    while ( y!=0 ) {
        z = x%y;
        x = y;
        y= z;
        num++;
    }
    gcd = x;
    
    return 0;
}