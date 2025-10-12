#include <iostream>
#include <string>

using namespace std;

int main()
{
    string n;
    int t;
    int sum = 0;

    cin >> t >> n;

    for (int i = 0; i < t; i++)
    {
        // cout << n[i] << endl;
        sum += (n[i] - '0');
    }

    cout << sum << endl;
}