#include <iostream>

using namespace std;

int main()
{
    int n;
    int maxValue = -1000001;
    int minValue = 1000001;
    int t;

    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> t;
        if (t > maxValue)
        {
            maxValue = t;
            // cout << "max : " << maxValue << endl;
        }

        if (t < minValue)
        {
            minValue = t;
        }
    }

    cout << minValue << " " << maxValue;

    return 0;
}