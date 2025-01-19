#include <iostream>
#include <string>

using namespace std;

int main()
{
    int t;
    int n;
    string s;

    cin >> t;

    for (int i = 0; i < t; i++)
    {
        cin >> n >> s;

        for (int k = 0; k < s.length(); k++)
        {
            for (int l = 0; l < n; l++)
            {
                cout << s[k];
            }
        }
        cout << endl;
    }
    return 0;
}