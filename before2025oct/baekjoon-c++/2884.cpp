#include <iostream>

using namespace std;

int main()
{
    int h;
    int m;

    cin >> h >> m;

    if (m >= 45)
    {
        m = m - 45;
    }
    else if (m < 45)
    {
        m = m + 15;
        h = h - 1;
    }

    if (h < 0)
    {
        h = 24 + h;
    }

    cout << h << " " << m << endl;

    return 0;
}
